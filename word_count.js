var filename = process.argv[2];
var fs = require('fs');
var data = fs.readFile(filename, function(err, data){
    if(data){
        var words = String(data).split(/\s+/);
        var map = words.reduce(function(hash, word, index, array){
            hash[word] = hash[word] ? hash[word] + 1 : 1;
            return hash;
        }, {})
        var sorted = Object.keys(map).sort(function(a, b){ return map[b] - map[a]});
        var text = sorted.reduce(function(lines, key){
            return lines += key + " : " + map[key] + "\n";
        }, "")
        fs.writeFile('book_out.txt', text);
    }
});
