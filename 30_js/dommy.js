// Tina Wong, Rubin Peci (Team NO FUN)
// SoftDev1 pd7
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-20

var addElement = function() {
  var ol = document.getElementById("thelist");
  var newElem = document.createElement("li");
  newElem.innerHTML = "WORD";
  ol.appendChild(newElem);
}

var fibonacci = function(n) {
  if(n < 2) {
    return n; // base case
  }
  else {
    return fibonacci(n-1) + fibonacci(n-2); // recursive case
  }
}

var countFib = 1;
var addFib = function() {
  var ol = document.getElementById("fiblist");
  var newFib = document.createElement("li");
  newFib.innerHTML = fibonacci(countFib);
  ol.appendChild(newFib);
  countFib++;
}

var button = document.getElementById('b');
button.addEventListener("click", addElement);

var fib = document.getElementById('fb');
fib.addEventListener("click", addFib);

var ol = document.getElementById("thelist");
ol.addEventListener('mouseover', function(e) {
  document.getElementById('h').innerHTML = e.target.innerHTML;
});
ol.addEventListener('mouseout', function(e) {
  document.getElementById('h').innerHTML = "Hello World!";
});
ol.addEventListener('click', function(e) {
  e.target.remove();
});
