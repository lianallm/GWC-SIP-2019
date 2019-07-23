// console.log("helloworld")

// var h1tag = document.getElementsByTagName("h1")[0];

var abouts = ["based in ny", "  born on october 5, 2002", "class of 2020"];

var pos = 0;

var loc = document.getElementById("about")

function changeAbo(){
  loc.innerHTML = abouts[pos]
  pos ++;
  if (pos >= abouts.length){
    pos = 0;
  }
}
var x = document.getElementsByTagName("body")[0]

function colorbg(){
  x.setAttribute("style", "background-color:blue")
}


x.setAttribute("onmousehover", colorbg());
