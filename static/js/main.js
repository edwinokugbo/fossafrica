const hamburger = document.getElementById("hamburger"),
  dropButton = document.getElementById("dropbtn"),
  mainElement = document.querySelector("main");
var navMenu = document.getElementById("nav-menu"),
  navDropMenu = document.getElementById("nav-drop-menu");

function toggleMenu() {
  navMenu.classList.toggle("show");
}

function dropMenu() {
  navDropMenu.classList.toggle("show");
}

function linkMain() {
  if (navDropMenu.classList.contains("show")) {
    navDropMenu.classList.remove("show");
  } else if (navMenu.classList.contains("show")) {
    navMenu.classList.remove("show");
  } else {
    location.href = "#/";
  }
}

hamburger.addEventListener("click", toggleMenu);
dropButton.addEventListener("click", dropMenu);
mainElement.addEventListener("click", linkMain);

var newChoiceButt = document.querySelector("#new-choice-butt");
var choiceBox = document.querySelector("#new-choice-box");
newChoiceButt.addEventListener("click", function () {
  if (choiceBox.style.display == "" || choiceBox.style.display == "none") {
    choiceBox.style.display = "block";
  } else {
    choiceBox.style.display = "none";
  }
});
