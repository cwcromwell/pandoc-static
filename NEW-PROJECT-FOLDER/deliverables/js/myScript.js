



var menuSelect = "#";

function injectContent () {

  console.log("injectContent function loaded");


var location = "<iframe src='askme.html" + menuSelect + "'></iframe>";

console.log("injectContent: location is: " + location);

document.getElementById('target').innerHTML=location
 }

injectContent();
