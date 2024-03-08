 const mntoggle = document.querySelector('.menu-toggle input');
 const nav = document.querySelector('nav ul');

mntoggle.addEventListener('click',function(){
    nav.classList.toggle('menushow');
})


function toggleMenu() {
  var menu = document.getElementById("menu");
  var burgerBars = document.querySelectorAll(".burger-menu .bar");
  
  if (menu.style.right === "0px") {
      menu.style.right = "-200px";
      burgerBars.forEach(bar => {
          bar.style.transform = "rotate(0)";
      });
  } else {
      menu.style.right = "0px";
      burgerBars.forEach(bar => {
          bar.style.transform = "rotate(45deg)";
      });
  }
  menu.classList.toggle('open'); // Toggle the 'open' class
}

