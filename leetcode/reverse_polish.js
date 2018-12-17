var assert = require('assert');

var evalRPN = function(tokens) {
    var numbers = [];
    while(tokens.length > 0){
        var t = tokens.shift();
        var n = parseInt(t);
        // if is a number
        if(!isNaN(n)){
            numbers.push(n);
        }
        // is an operator
        else{
            var b = numbers.pop();
            var a = numbers.pop();
            var res;
            switch(t){
                case '+':
                    res = a + b;
                    break;
                case '-':
                    res = a - b;
                    break;
                case '*':
                    res = a * b;
                    break;
                case '/':
                    res = Math.trunc(a / b);
                    break;
                default:
                    res = 0;
            }
            numbers.push(res);
        }
    }

    return numbers.pop();
};

assert.equal(evalRPN(["2", "1", "+", "3", "*"]), 9);
assert.equal(evalRPN(["4", "13", "5", "/", "+"]), 6);
assert.equal(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22);

