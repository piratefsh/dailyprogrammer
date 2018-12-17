const fs = require('fs');

function solve(input, dict, minWordLength) {
    function isValid(chars, lastWordPartial) {
        if (chars.length === 0) return true;
        if (lastWordPartial && new RegExp('^' + chars, 'im').test(dict)) return true;
        for (var i = minWordLength || 3; i <= chars.length; i++) {
            if (new RegExp('^' + chars.slice(0, i) + '$', 'im').test(dict)
                && isValid(chars.slice(i), lastWordPartial)) return true;
        }
        return false;
    }

    function decode(input, prefix) {
        console.log(prefix, isValid(prefix, true))
        if (input.length === 0) return isValid(prefix) ? [prefix] : [];
        if (!isValid(prefix, true)) return [];  // prune tree early on

        var words = [], doubleDigit = +input.slice(0, 2)
        if (doubleDigit >= 10 && doubleDigit <= 26)
            words = words.concat(decode(input.slice(2), prefix + String.fromCharCode(doubleDigit + 64)));
        if (input[0] > 0)
            words = words.concat(decode(input.slice(1), prefix + String.fromCharCode(+input[0] + 64)));
        return words;
    }

    console.log(decode(String(input), '').join('\n') || 'No solutions found');
}

var input = '85121215231518124';
solve(input, fs.readFileSync('enable1.txt').toString(), 5)
