"use strict";

const fs = require('fs');

class LetterSplits{
    constructor(minWordLength){
        // create mapping 1-A ... 26-Z
        this.mapping = {};
        for(let i = 0; i < 26; i++){
            this.mapping['' + (i + 1)] = String.fromCharCode(65 + i);
        }

        this.dict = {};
        this.data = fs.readFileSync('enable1.txt').toString();

        // save dict by 2 letter prefix
        this.data.split('\n').forEach((word) => {
            const prefix = word.slice(0, 2);
            if(!(prefix in this.dict)){
                this.dict[prefix] = [word.trim()];
            }
            else{
                this.dict[prefix].push(word.trim());
            }
        })
        this.minWordLength = minWordLength || 3;
    }

    lookup(word){
        if(word.length < 2) return false;

        word = word.toLowerCase();
        const prefix = word.slice(0, 2);
        return prefix in this.dict && this.dict[prefix].indexOf(word) > -1;
    }

    split(word){
        const splits = [];
        for(let i = this.minWordLength; i < word.length + 1; i++){
            splits.push([word.slice(0, i), word.slice(i)]);
        }
        return splits;
    }

    valid(partial, partialMatch){
        if(partial.length == 0){
            return true;
        }

        if(partialMatch && new RegExp(`^${partial}`, 'im').test(this.data)){
            return true;
        }

        // else find segments
        for(let i = this.minWordLength; i < partial.length + 1; i++){
            let first = partial.slice(0, i)
            let rest = partial.slice(i)

            // if is valid substring (exists in dictionary)
            if(new RegExp(`^${first}$`, 'im').test(this.data)){
                // find if rest of string is valid
                if(this.valid(rest, partialMatch)){
                    return true;
                }
            }
        }
        return false;
    }

    decode(integers, validate){
        const candidates = this.decodeCandidates(integers, "", validate);
        return candidates;
    }

    decodeCandidates(integers, currWord, validate){
        let words = [];

        // reached end of integer
        if(integers.length == 0){
            if(validate){
                if(this.valid(currWord)){
                    words.push(currWord);
                }
            }
            else{
                words.push(currWord);
            }
            return words;
        }

        if(validate && currWord.length > 0 && !this.valid(currWord, true)){
            return words;
        }

        // if valid first digit (non-zero)
        if(integers[0] in this.mapping){
            // add char for first digit to currWord, find rest of decoding
            const w1 = currWord + this.mapping[integers[0]]
            words = words.concat(this.decodeCandidates(integers.slice(1), w1, validate));

            // if has second digit
            if(integers.length > 1){
                // check if double digit is valid char
                const doubleDigit = parseInt(integers.slice(0, 2));
                if(doubleDigit < 26){
                    // add char for double digit to currWord, find rest of decoding
                    const w2 = currWord + this.mapping[doubleDigit]
                    words = words.concat(this.decodeCandidates(integers.slice(2), w2, validate));
                }
            }
        }

        return words;
    }
}


module.exports = LetterSplits;