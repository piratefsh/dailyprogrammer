#Task: Bahasa F

## Description

Every Malaysian student learns how to speak a secret language called 'Bahasa F' derived from the Malay language. It sounds mysterious, but is actually quite easy to learn!

For example, a word in Malay, 'saya' is translated to Bahasa F as 'sa __fa__ ya __fa__'.

It works by changing the consonant in every syllable (sukukata) to 'f' and adding right after that syllable. If the syllable does not have a consonant, just add 'f' before it.

In Malay:

```
Saya suka kek ini
```

In Bahasa F:

```
Safayafa sufukafa kekfek ifinifi
```


## Task
Given a sentence string in Malay, translate it to Bahasa F. To make it easier for you, we have separated out each syllable with backslashes `/`. Individual words are separated by spaces. You will need to keep the uppercase letters where they occur. 

## Input and Output

### Example input
```
Cu/a/ca ha/ri i/ni san/gat pa/nas
```

### Example Output
```
Cufuafacafa hafarifi ifinifi sanfangatfat pafanasfas
```

## Task author's notes
Will have to think about how to generate large test cases and automate the syllable separation. Inspired by [Challenge #212](https://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/) of dailyprogrammer.
