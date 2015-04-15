    // file reading stuff
    var filename = process.argv[2];
    var fs = require('fs');
    var data = fs.readFileSync(filename, {encoding: 'ascii'});
    if(data){
        var pairs = data.split('\n');
        pairs.forEach(function(pair){
            var each = pair.split(" ");
            for(var i = 0; i < each.length; i++){
                each[i] = parseInt(each[i]) >>> 0;
            }
            findCompatibility(each);
        });
    }

    function findCompatibility(couple){
        var compatibility = numOfOnes(~(couple[0] ^ couple[1]));
        var common = compatibility/(32.0) * 100.0;
        console.log(common + '%');
        console.log(couple[0] + ' should avoid ' + (~couple[0]>>>0))
        console.log(couple[1] + ' should avoid '  + (~couple[1]>>>0) + "\n")
    }

    function decToBin(dec){
        return dec.toString(2);
    }

    function numOfOnes(num){
        var count = 0;
        while(num != 0){
            num = num & (num - 1);
            count++;
        }
        return count;
    }