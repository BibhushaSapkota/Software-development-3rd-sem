
function myFunction(id) {

   let navLink = Array.from(document.getElementsByClassName('nav-link'));
   navLink.forEach(element => {
      console.log(element.removeAttribute('style'))
   });

   document.getElementById(id).style.color = "red";
   document.getElementById(id).style.fontSize = "30px";
}

function reveal() {
   var reveals = document.querySelectorAll(".reveal");
 
   for (var i = 0; i < reveals.length; i++) {
     var windowHeight = window.innerHeight;
     var elementTop = reveals[i].getBoundingClientRect().top;
     var elementVisible = 150;
 
     if (elementTop < windowHeight - elementVisible) {
       reveals[i].classList.add("active");
     } else {
       reveals[i].classList.remove("active");
     }
   }
 }
 
 window.addEventListener("scroll", reveal);

 /* image slider*/
 window.onload = function() {

  let slider = document.querySelector('#slider');
  let move = document.querySelector('#move');
  let moveLi = Array.from(document.querySelectorAll('#slider #move li'));
  let forword = document.querySelector('#slider #forword');
  let back = document.querySelector('#slider #back');
  let counter = 1;
  let time = 3000;
  let line = document.querySelector('#slider #line');
  let dots = document.querySelector('#slider #dots');
  let dot;

  for (i = 0; i < moveLi.length; i++) {

      dot = document.createElement('li');
      dots.appendChild(dot);
      dot.value = i;
  }

  dot = dots.getElementsByTagName('li');

  line.style.animation = 'line ' + (time / 1000) + 's linear infinite';
  dot[0].classList.add('active');

  function moveUP() {

      if (counter == moveLi.length) {

          moveLi[0].style.marginLeft = '0%';
          counter = 1;

      } else if (counter >= 1) {

          moveLi[0].style.marginLeft = '-' + counter * 100 + '%';
          counter++;
      } 

      if (counter == 1) {

          dot[moveLi.length - 1].classList.remove('active');
          dot[0].classList.add('active');

      } else if (counter > 1) {

          dot[counter - 2].classList.remove('active');
          dot[counter - 1].classList.add('active');

      }

  }

  function moveDOWN() {

      if (counter == 1) {

          moveLi[0].style.marginLeft = '-' + (moveLi.length - 1) * 100 + '%';
          counter = moveLi.length;
          dot[0].classList.remove('active');
          dot[moveLi.length - 1].classList.add('active');

      } else if (counter <= moveLi.length) {

          counter = counter - 2;
          moveLi[0].style.marginLeft = '-' + counter * 100 + '%';   
          counter++;

          dot[counter].classList.remove('active');
          dot[counter - 1].classList.add('active');

      }  

  }

  for (i = 0; i < dot.length; i++) {

      dot[i].addEventListener('click', function(e) {

          dot[counter - 1].classList.remove('active');
          counter = e.target.value + 1;
          dot[e.target.value].classList.add('active');
          moveLi[0].style.marginLeft = '-' + (counter - 1) * 100 + '%';

      });

  }

  forword.onclick = moveUP;
  back.onclick = moveDOWN;

  let autoPlay = setInterval(moveUP, time);

  slider.onmouseover = function() {

      autoPlay = clearInterval(autoPlay);
      line.style.animation = '';

  }

  slider.onmouseout = function() {

      autoPlay = setInterval(moveUP, time);
      line.style.animation = 'line ' + (time / 1000) + 's linear infinite';

  }

}
