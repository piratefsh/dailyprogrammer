var LetterSplits = require('./letter-splits');

module.exports =
{
    mappingGenerated: function(test){
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
    }
} 
