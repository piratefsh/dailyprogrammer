var util = require('util')
var message = process.argv[2]
    var encoded = message.replace(/([^aeiouåäöAEIOUYÅÄÖ\.\?!\s])/gi, function(match, p1){
        return p1 + "o" + p1.toLowerCase();
    });
    console.log(encoded)