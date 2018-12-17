function intToRomanTask(){
    var mapping = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    var divisors = Object.keys(mapping)
                        .sort(function(a, b){
                            return parseInt(a) > parseInt(b);})
                        .reverse()
                        .map(function(e, i){
                            return parseInt(e)});

    console.log(divisors);
    var intToRoman = function(num) {
        res = "";
        while(num > 0){
            console.log(num)
            for(var d of divisors){
                if(d <= num){
                    num = num - d;
                    res += mapping[d];
                    break;
                }
            }
        }
        return res;
    };



    console.log(intToRoman(220))
}


function romanToIntTask(){

    var mapping = {
        'I' : 1,
        'IV' : 4,
        'V' : 5,
        'IX' : 9,
        'X' : 10,
        'XL' : 40,
        'L' : 50,
        'XC' : 90,
        'C' : 100,
        'CD' : 400,
        'D' : 500,
        'CM' : 900,
        'M' : 1000
    }


    var romanToInt = function(s) {
        var i = 0;
        var total = 0;
        while(s.length > 0){
            var two = s.slice(i, 2);
            var one = s.slice(i, 1);
            if (two in mapping){
                total += mapping[two];
                s = s.slice(i + 2 );
            }
            else if (one in mapping){
                total += mapping[one];
                 s = s.slice(i + 1 );
            }
            
        }
        return total;
    };


    console.log(romanToInt('II'))
    console.log(romanToInt('CCXX'))
}
intToRomanTask()
romanToIntTask()