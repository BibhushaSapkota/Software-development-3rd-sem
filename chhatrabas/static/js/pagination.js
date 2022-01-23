$(document).ready(function(){

  initSliders();

  //NOTE: To append in different container
  var appendToContainer = function(htmlele, record){
    console.log(record)
  };

  var afterFilter = function(result, jQ){
    $('#total_hostels').text(result.length);

    var checkboxes  = $("#genre_criteria :input:gt(0)");

    checkboxes.each(function(){
      var c = $(this), count = 0

      if(result.length > 0){
        count = jQ.where({ 'genre': c.val() }).count;
      }
      c.next().text(c.val() + '(' + count + ')')
    });
  }

  var FJS = FilterJS(hostels, '#hostels', {
    template: '#hostel-template',
    search: { ele: '#searchbox' },
    //search: {ele: '#searchbox', fields: ['Price']}, // With specific fields
    callbacks: {
      afterFilter: afterFilter 
    },
    pagination: {
      container: '#pagination',
      visiblePages: 5,
      perPage: {
        values: [12, 15, 18],
        container: '#per_page'
      },
    }
  });

  FJS.addCallback('beforeAddRecords', function(){
    if(this.recordsCount >= 450){
      this.stopStreaming();
    }
  });

  FJS.addCallback('afterAddRecords', function(){
    var percent = (this.recordsCount - 250)*100/250;

    $('#stream_progress').text(percent + '%').attr('style', 'width: '+ percent +'%;');

    if (percent == 100){
      $('#stream_progress').parent().fadeOut(1000);
    }
  });

  FJS.setStreaming({
    data_url: 'data/stream_hostels.json',
    stream_after: 1,
    batch_size: 50
  });

  FJS.addCriteria({field: 'roommate', ele: '#roommate_filter', type: 'range', all: 'all'});
  FJS.addCriteria({field: 'rating', ele: '#rating_filter', type: 'range'});
  FJS.addCriteria({field: 'Price', ele: '#Price_filter', type: 'range'});
  FJS.addCriteria({field: 'genre', ele: '#genre_criteria input:checkbox'});
  

  /*
   * Add multiple criterial.
    FJS.addCriteria([
      {field: 'genre', ele: '#genre_criteria input:checkbox'},
      {field: 'roommate', ele: '#roommate_filter', type: 'range'}
    ])
  */

  window.FJS = FJS;
});

function initSliders(){
  $("#rating_slider").slider({
    min: 1,
    max: 5,
    values:[1, 5],
    step: 1,
    range:true,
    slide: function( event, ui ) {
      $("#rating_range_label" ).html(ui.values[ 0 ] + ' - ' + ui.values[ 1 ]);
      $('#rating_filter').val(ui.values[0] + '-' + ui.values[1]).trigger('change');
    }
  });

  $("#Price_slider").slider({
    min: 5000,
    max: 20000,
    values:[0, 20000],
    step: 1,
    range:true,
    slide: function( event, ui ) {
      $("#Price_range_label" ).html(' Rs: ' + ui.values[ 0 ] + ' - ' + ' Rs: '+ ui.values[ 1 ]);
      $('#Price_filter').val(ui.values[0] + '-' + ui.values[1]).trigger('change');
    }
  });


  $('#genre_criteria :checkbox').prop('checked', true);
  $('#all_genre').on('click', function(){
    $('#genre_criteria :checkbox').prop('checked', $(this).is(':checked'));
  });
}
