
document.addEventListener("DOMContentLoaded", function() {
  var menu = document.getElementById("menu");
  var mobNav = document.getElementById("mobNav");
  menu.addEventListener("click", function() {
    if (mobNav.style.display === "none" || mobNav.style.display === "") {
      mobNav.style.display = "flex";
      menu.style.rotate=`45deg`;
      menu.style.scale=`0.69`;
      menu.style.cursor=`unset`;
      menu.style.borderWidth=`1px`;
      menu.style.borderBlockColor=`red`;
      menu.style.borderBlockStyle=`dashed`
    } else {
      mobNav.style.display = "none";
      menu.style.rotate=`0deg`;
      menu.style.scale=`1 `;
      menu.style.cursor=` unset`;
      menu.style.borderWidth=` 0px`;
      menu.style.borderBlockColor=` transparent`;
      menu.style.borderBlockStyle=` none`
    }
  });
});


       function scrollToElement(id) {
            var element = document.getElementById(id);
            if (element) {
                var offset = element.getBoundingClientRect().top;
                window.scrollBy({
                    top: offset - 5 * parseFloat(getComputedStyle(document.documentElement).fontSize),
                    behavior: 'smooth'
                });
            }
        }
 