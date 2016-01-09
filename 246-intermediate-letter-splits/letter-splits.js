"use strict";

const fs = require('fs');

class LetterSplits{
    constructor(minWordLength){
        // create mapping 1-A ... 26-Z
        this.mapping = {};
        for(let i = 0; i < 26; i++){
            this.mapping['' + (i + 1)] = String.fromCharCode(65 + i);
        }

        this.dict  = fs.readFileSync('enable1.txt').toString();
        this.minWordLength = minWordLength || 3
    }

    valid(partial){
        if(partial.length == 0){
            return true;
        }

        const wholeRe = new RegExp(`^${partial}$`, 'im');

        // if whole word exists, consider found
        if(wholeRe.test(this.dict)){
            return true;
        }

        // else find substrings
        for(let i = this.minWordLength; i < partial.length+1; i++){
            // if is valid substring (exists in dictionary)
            const substr = partial.slice(0,i);
            const re = new RegExp(`^${substr}$`, 'im');
            if(re.test(this.dict)){
                // find if rest of string is valid
                if(this.valid(partial.slice(i))){
                    return true;
                }
            }
        }
        return false;
    }

    decode(integers, validate, currWord){
        currWord = currWord || "";

        let words = [];

        // reached end of integer
        if(integers.length == 0){
            // validate if necessary
            if(validate) {
                if(this.valid(currWord)){
                    words.push(currWord);
                }
            }
            else{
                words.push(currWord);
            }

            return words;
        }

        // if valid first digit (non-zero)
        if(integers[0] in this.mapping){
            // add char for first digit to currWord, find rest of decoding
            words = words.concat(this.decode(integers.slice(1), validate,
                currWord + this.mapping[integers[0]]));

            // if has second digit
            if(integers.length > 1){
                // check if double digit is valid char
                const doubleDigit = parseInt(integers.slice(0, 2));
                if(doubleDigit < 26){
                    // add char for double digit to currWord, find rest of decoding
                    words = words.concat(this.decode(integers.slice(2), validate,
                        currWord + this.mapping[doubleDigit]));
                }
            }
        }

        return words;
    }
}


module.exports = LetterSplits;