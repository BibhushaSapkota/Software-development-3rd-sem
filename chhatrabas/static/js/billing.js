function computeDuration(){
    var from = new Date(document.getElementById("from").value);
    var to = new Date(document.getElementById("to").value);
      days=1000*60*60*24;
    diff=(to-from)/days+1;
    document.getElementById("computeDuration").innerHTML = diff;
  
    
}
  
function price(){
    var price = document.getElementById("cost").value;
    console.log(price)
    total_price = Math.floor((Number(price)/30)*diff)
    document.getElementById("price").innerHTML = total_price;
     
}

function pricefield(){
    var pricefield = document.getElementById("cost").value;
    console.log(pricefield)
    total_price = Math.floor((Number(pricefield)/30)*diff)
    document.getElementById("pricefield").value = total_price;
  
}


