// Tina Wong, Rubin Peci (Team NO FUN)
// SoftDev1 pd7
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-20

// add a new list element to thelist with WORD displayed
var addElement = function() {
  var ol = document.getElementById("thelist");
  var newElem = document.createElement("li");
  newElem.innerHTML = "WORD";
  ol.appendChild(newElem);
}

// fib function
var fibonacci = function(n) {
  if(n < 2) {
    return n; // base case
  }
  else {
    return fibonacci(n-1) + fibonacci(n-2); // recursive case
  }
}

// add the next Fib number as the next list element for the Fib list
var countFib = 0;
var addFib = function() {
  var ol = document.getElementById("fiblist");
  var newFib = document.createElement("li");
  newFib.innerHTML = fibonacci(countFib);
  ol.appendChild(newFib);
  countFib++;
}

var button = document.getElementById('b');

// when the button is clicked, call the addElement function
button.addEventListener("click", addElement);

var fib = document.getElementById('fb');

// when the fib button is clicked, call the addFib function
fib.addEventListener("click", addFib);

var ol = document.getElementById("thelist");

// when the mouse is over a list element, change the heading to the content of the list element
ol.addEventListener('mouseover', function(e) {
  document.getElementById('h').innerHTML = e.target.innerHTML;
});

// when the mouse is not on a list element, revert the heading to 'Hello World!'
ol.addEventListener('mouseout', function(e) {
  document.getElementById('h').innerHTML = "Hello World!";
});

// when the item is clicked, remove it
ol.addEventListener('click', function(e) {
  e.target.remove();
});
