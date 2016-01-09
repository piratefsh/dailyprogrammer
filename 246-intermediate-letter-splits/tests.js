var LetterSplits = require('./letter-splits');

module.exports =
{
    'mapping generated correctly': function(test){
        console.log(LetterSplits);
        var ls = new LetterSplits();
        var numLetters = Object.keys(ls.mapping).length;
        test.equal(numLetters, 26, 'mapping contains 26 characters');
        test.equal(ls.mapping[26], 'Z', '26 maps to Z');
        test.done();
    },

    decode: function(test){
        var ls = new LetterSplits();
        var res = ls.decode(new String(1234));
        res.sort();
        test.equal(res.length , 3, 'found 3 results for 1234');
        test.equal(res[0], 'ABCD', 'found ABCD');
        test.equal(res[1], 'AWD', 'found AWD');
        test.equal(res[2], 'LCD', 'found LCD');
        test.done();
    },

    'test case: 1234567899876543210': function(test){
        var ls = new LetterSplits();
        var res = ls.decode('1234567899876543210');
        var resstr = res.sort().join(',');
        var expected = 'LCDEFGHIIHGFEDCBJ,AWDEFGHIIHGFEDCBJ,ABCDEFGHIIHGFEDCBJ'.split(',').sort().join();
        test.equal(resstr, expected, 'found expected answer');
        test.done();
    },

    'test case: JET': function(test){
        var ls = new LetterSplits();
        var res = ls.decode('10520');
        var expected = 'JET';
        test.equal(res.length, 1, 'found one result');
        test.equal(res[0], expected, 'found expected answer');
        test.done();
    },
    
    'splits': function(test){
        
        var ls = new LetterSplits(1);
        var res = ls.split('abc');
        test.equal(res.length, 3, 'split into 3');
        test.ok(res[0].indexOf('a') > -1 && res[0].indexOf('bc') > -1 , 'split into 3');
        test.ok(res[1].indexOf('ab') > -1 && res[1].indexOf('c') > -1 , 'split into 3');
        test.ok(res[2].indexOf('abc') > -1 && res[2].indexOf('') > -1 , 'split into 3');
        test.done();
    },

    'test validation': function(test){
        var ls = new LetterSplits();
        test.ok(ls.valid('ACUTE'), 'ACUTE is valid word');
        test.ok(!ls.valid('MBATE'), 'MDATE is not a valid word');
        test.done();
    },
    
    'test case: 1321205': function(test){
        var ls = new LetterSplits();
        var res = ls.decode('1321205', true);
        var resstr = res.sort().join(',');
        var expected = 'ACUTE,MUTE'.split(',').sort().join();
        test.equal(resstr, expected, 'found expected answer');
        test.done();
    },

    'test case: 1252020518': function(test){
        var ls = new LetterSplits();
        var res = ls.decode('1252020518', true);
        var resstr = res.sort().join(',');
        var expected = 'LETTER,ABETTER'.split(',').sort().join();
        test.equal(resstr, expected, 'found expected answer');
        test.done();
    },

    'HELLOWORLD': function(test){
        var ls = new LetterSplits(4);
        var res = ls.decode('85121215231518124', true);
        var resstr = res.sort().join(',');
        var expected = 'HELLOWORLD'.split(',').sort().join();
        test.equal(resstr, expected, 'found expected answer');
        test.done();
    },


    'bonus': function(test){
        var ls = new LetterSplits(5);
        var res = ls.decode('81161625815129412519419122516181571811313518', true);
        test.equal(res.length, 1, 'found answer: ' + res);
        test.done();
    }
} 
