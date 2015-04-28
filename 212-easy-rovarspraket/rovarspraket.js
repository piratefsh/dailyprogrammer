// Challenge: http://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/

var util    = require('util')
var mode    = process.argv[3]
var message = process.argv[2]

if(mode == "encode"){
    var encoded = message.replace(/([^aeiouåäöAEIOUYÅÄÖ\.\?!\s])/gi, function(match, p1){
        return p1 + "o" + p1.toLowerCase();
    });
    console.log(encoded);
}

else if(mode =="decode"){
    var decoded = message.replace(/([^aeiouåäöAEIOUYÅÄÖ\.\?!\s])o\1/gi, "$1");
    console.log(decoded); 
}