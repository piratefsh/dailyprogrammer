"use strict";
class LetterSplits{
    constructor(){
        // create mapping
        this.mapping = {};
        for(let i = 0; i < 26; i++){
            const char = String.fromCharCode(65 + i);
            this.mapping['' + (i + 1)] = char;
        }
    }

    decode(integers, currWord){
        currWord = currWord || "";
        let words = [];

        if(integers.length == 0){
            words.push(currWord);
            return words;
        }
        else if(integers.length == 1){
            if(integers in this.mapping){
                words.push(currWord + this.mapping[integers]);
            }
            return words;
        }

        // if valid first digit
        if(integers[0] in this.mapping){
            // concat first digit
            words = words.concat(this.decode(integers.slice(1), currWord + this.mapping[integers[0]]));

            // check if double digit is valid char
            const doubleDigit = parseInt(integers.slice(0, 2));
            if(doubleDigit < 26){
                words = words.concat(this.decode(integers.slice(2), currWord + this.mapping[doubleDigit]));
            }
        }

        return words;
    }
}


module.exports = LetterSplits;