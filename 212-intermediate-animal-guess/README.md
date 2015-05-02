# Animal Guessing Game
Program that tries to guess what animal you're thinking of and learns if it doesn't get it right. Uses a binary tree as described [here](http://openbookproject.net/py4fun/animal/animal.html).

Stores and reads tree from `animal.json` after each round.

Challenge 212 Intermediate on [r/dailyprogrammer](http://www.reddit.com/r/dailyprogrammer/comments/34asls/20150429_challenge_212_intermediate_animal_guess/).

## Run

```
python3 animal_guess.py
```

## Sample output

```
is it an animal?y
does it bark?y
Are you thinking of a dog? y
Thanks for playing!

is it an animal?y
does it bark?n
does it swim?y
is it scaley?n
Are you thinking of a octopus? y
Thanks for playing!

is it an animal?y
does it bark?y
Are you thinking of a dog? n
Oh dear, what was the right answer? wolf
What is a question that distinguishes wolf from dog? is it tame?
What would the answer be for wolf? n
```