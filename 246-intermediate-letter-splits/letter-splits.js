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
        const data = fs.readFileSync('enable1.txt').toString();

        // save dict by 2 letter prefix
        data.split('\n').forEach((word) => {
            const prefix = word.slice(0, 2);
            if(!(prefix in this.dict)){
                this.dict[prefix] = [word.trim()];
            }
            else{
                this.dict[prefix].push(word.trim());
            }
        })
        this.minWordLength = minWordLength || 3;

        this.tested = {};
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

    valid(partial){
        if(partial.length == 0){
            return true;
        }

        // else find segments
        const segments = this.split(partial);
        for(let segment of segments){
            let first = segment[0];
            let rest = segment[1];

            // if is valid substring (exists in dictionary)

            // lookup if has been searched
            if(first in this.tested && this.tested[first]){
                if(this.valid(rest)){
                    return true;
                }
            }

            else{
                const exists = this.lookup(first);
                if(exists){
                    // find if rest of string is valid
                    if(this.valid(rest)){
                        return true;
                    }
                }
                // save result
                this.tested[first] = exists;
            }
        }
        return false;
    }

    decode(integers, validate){
        const candidates = this.decodeCandidates(integers, "");
        // return as is if no validation
        if(!validate){
            return candidates;
        }

        // else do validation
        const results = [];
        return candidates.filter((candidate, i)=>{
            return this.valid(candidate);
        });
    }

    decodeCandidates(integers, currWord){

        let words = [];

        // reached end of integer
        if(integers.length == 0){
            // validate if necessary
            words.push(currWord);

            return words;
        }

        // if valid first digit (non-zero)
        if(integers[0] in this.mapping){
            // add char for first digit to currWord, find rest of decoding
            const w1 = currWord + this.mapping[integers[0]]
            words = words.concat(this.decodeCandidates(integers.slice(1), w1));

            // if has second digit
            if(integers.length > 1){
                // check if double digit is valid char
                const doubleDigit = parseInt(integers.slice(0, 2));
                if(doubleDigit < 26){
                    // add char for double digit to currWord, find rest of decoding
                    const w2 = currWord + this.mapping[doubleDigit]
                    words = words.concat(this.decodeCandidates(integers.slice(2), w2));
                }
            }
        }

        return words;
    }
}


module.exports = LetterSplits;