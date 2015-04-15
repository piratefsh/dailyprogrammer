var arg1 = process.argv[2]>>>0, arg2 = process.argv[3]>>>0;
function match_strength(a,b) {
    sum = 0;
    for (i=0;i<32;i++){ sum += ( Math.pow(2,i) & ~ ( a ^ b )) ? 1: 0; }
    return sum/0.32;
}
console.log(arg1 + " in binary is " + arg1.toString(2));
console.log(arg2 + " in binary is " + arg2.toString(2));
console.log(match_strength(arg1,arg2) + "% Compatibility");
console.log(arg1 + " should avoid " + ((~arg1)>>>0) );
console.log(arg2 + " should avoid " + ((~arg2)>>>0) );