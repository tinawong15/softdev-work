// Tina Wong, Rubin Peci
// SoftDev1 pd7
// K28 -- Sequential Progression
// 2018-12-18

var fibonacci = function(n) {
  if(n < 2) {
    return n; // base case
  }
  else {
    return fibonacci(n-1) + fibonacci(n-2); // recursive case
  }
}

var gcd = function(a,b) {
  if(b != 0) {
    return gcd(b, a % b); // recursive case
  }
  else {
    return a; // base case
  }
}

// helper function for randomStudent() generates a list of students when a length is given
var generateList = function(length) {
  var list = []
  for(i = 0; i < length; i++) {
    list.push("Student "+i) // append to list
  }
  return list;
}

var students = generateList(5); // call function generateList() and bind the value to students variable

var randomStudent = function() {
    var index = Math.floor(Math.random() * students.length); // get random index for list
    return students[index];
}
