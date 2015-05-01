#!/usr/bin/env python3
from operator import attrgetter

class Animal:
    def __init__(self, name):
        self.name = name
        self.questions = set([])
        self.points = 0

animal_data = [line for line in open(".animal_data", "r").read().split("\n") if line != ""]

animals, questions = [], set()
for line in animal_data:
    if line.endswith(":"):
        animals.append(Animal(line[:-1]))
    else:
        animals[-1].questions.add(line)
        questions.add(line)

while input("Think of an animal and type 'y' to begin: ").upper()[0] != "Y": pass

for i in range(5):
    question = questions.pop() + " "
    if input(question).upper()[0] == "Y":
        for animal in [animal for animal in animals if question[:-1] in animal.questions]:
            animal.points += 1   

print("Were you thinking of a ", max(animals, key=attrgetter("points")).name, "? ", sep="", end="")
if input().upper()[0] == "Y":
    print("Thanks for playing!")
else:
    animal = input("What animal were you thinking of? ")
    new_question = input("Enter a new question that you would have answered 'yes' to: ")

    inserted = False
    for i in range(len(animal_data)):
        if animal_data[i] == animal + ":":
            animal_data.insert(i + 1, new_question)
            inserted = True
            break
    if not inserted:
        animal_data.append(animal + ":")
        animal_data.append(new_question)

    data_file = open(".animal_data", "w")
    for line in animal_data:
        data_file.write(line + "\n")