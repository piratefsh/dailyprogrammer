var util = require('util')

var name = process.argv[2]
var groups = name.match(/^([^AEIOU]?)(.*)/i);
var first = groups[1] + ""; 
var stripped = groups[2].toLowerCase();
var prefixes = { 'b': 'B', 'm': 'M', 'f': 'F'};
var prefix = 'o-';

for (var c in prefixes){
    var regex = new RegExp('[' + c + ']', 'i');
    if(first.match(regex)){
        prefixes[c] = prefixes[c]+prefix;
    }
    else{
        prefixes[c] = prefixes[c];
    }
}
console.log(util.format("%s, %s, bo %s%s", name, name, prefixes['b'], stripped))
console.log(util.format("Bonana fanna fo %s%s", prefixes['f'], stripped))
console.log(util.format("Fee fy mo %s%s", prefixes['m'], stripped))
console.log(util.format("%s!"), name)
