
var abouts = ["~based in ny~", " ~born on october 5, 2002~", "~class of 2020~", "~living the minimalist life~"];

var pos = 0;

var loc = document.getElementById("about")

function changeAbo(){
  loc.innerHTML = abouts[pos]
  pos ++;
  if (pos >= abouts.length){
    pos = 0;
  }
}

//compser change
var composerlist = ["~beethoven~", " ~chopin~", "~schumann~", "~cloude debussy~", "~john williams~","~dvorak~", "~george gershwin~"];

var pos1 = 0;

var loc1 = document.getElementById("composer")

function changeCom(){
  loc1.innerHTML = composerlist[pos1]
  pos1 ++;
  if (pos1 >= composerlist.length){
    pos1 = 0;
  }
}



var composerpics = ["https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTI2NTgyMzIxOTcyMjU5NDU5/beethoven-600x600jpg.jpg", "https://assets.classicfm.com/2017/45/frederic-chopin-1509969944-list-tablet-0.jpg", "https://www.mphil.de/fileadmin/_processed_/csm_Schumann_Robert_610ce93646.jpg", "~cloude debussy~", "~john williams~","~dvorak~", "~george gershwin~"];

var pos1 = 0;

var loc1 = document.getElementById("image")

function changeImg(){
  loc1.innerHTML = composerlist[pos1]
  pos1 ++;
  if (pos1 >= composerlist.length){
    pos1 = 0;
  }
}

// document.getElementbyId("about")
/*
var i = 0;
for (i = 0; i < 21; i++) {
  console.log(i)
}

i = 0 // sets i to 0
while(i <= 20){ //runs when i <= 20
  console.log(i);
  i +=2; //adds 2 to each iteration
}

i = 0;
while(i <= 20){
  if(i % 2 == 0){
    console.log(i) //runs if i is even
  }
  i += 1; //adds 1 to i each iteration
}

function getTemp(type){
  if (type =="c"){
    return 22.5;
  }
  if (type =="f"){
    return 100;
  }
}

console.log(getTemp("f"))
console.log(getTemp("c"))
*/
