# Question tree node
class Node:
    def __init__(self, content):
        self.content = content
        self.yes = None # child nodes for 'y' and 'n' answers
        self.no = None
    def getNext(self, answer):
        if answer is 'y':
            return self.yes
        return self.no

# initialize tree with single question and animal
init_leaf   = Node('Cat')
root        = Node('Are you thinking of an animal? ')
root.yes    = init_leaf

while True:
    # start from root node, travel down tree
    curr        = root
    while True:
        prev     = curr
        response = input(curr.content)
        curr     = curr.getNext(response)
        if not curr.getNext(response):
            break
     
    prev_response = response 

    # check if we guessed animal correctly  
    guessed_animal = curr.content
    response = input('Are you thinking of a %s? ' % gus)

    # guessed right
    if response == 'y':             
        print('Thanks for playing!')

    # guessed wrongly
    else:                           
        new_animal = input('Oh dear, what was the right answer? ')
        new_question = input('What is a question that distinguishes %s from %s? ' % new_animal, guessed_animal)
        new_animal_response = input('What would the answer be for %s? ' % new_animal)

        # add new question
        new_node    = Node(new_question + " ")
        if new_animal_response == 'y':
            new_node.yes = Node(new_animal)
            new_node.no = curr
        else:
            new_node.no = Node(new_animal)
            new_node.yes = curr

        if prev_response == 'y':
            prev.yes    = new_node
            prev.no     = curr
        else:
            prev.no    = new_node
            prev.yes     = curr
