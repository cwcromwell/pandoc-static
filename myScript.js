



var menuSelect = "#heading-three";

function injectContent () {

  console.log("injectContent function loaded");


var location = "<iframe src='build/testdoc.html" + menuSelect + "'></iframe>";

console.log("injectContent: location is: " + location);

document.getElementById('target').innerHTML=location
 }

injectContent();
