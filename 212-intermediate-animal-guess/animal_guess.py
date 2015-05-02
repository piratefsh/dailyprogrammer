from pprint import pprint
import json

savefile = 'animals.json'

# Question tree node
class Node:
    def __init__(self, content):
        self.content = content.strip()
        self.yes = None # child nodes for 'y' and 'n' answers
        self.no = None
    def getNext(self, answer):
        if answer is 'y':
            return self.yes
        return self.no
    def hasNext(self):
        return self.yes or self.no
    def __repr__(self):
        return self.content

def tree_to_map(node):
    if node is None:
        return None 
    curr = {
        'content': node.content,
        'yes' : tree_to_map(node.yes),
        'no' : tree_to_map(node.no)
    }
    return curr

def map_to_tree(node):
    if node is None:
        return None
    curr = Node(node["content"])
    curr.yes = map_to_tree(node["yes"]) if "yes" in node else None
    curr.no = map_to_tree(node["no"]) if "no" in node else None
    return curr

def load():
    f = open(savefile, 'r')
    return map_to_tree(json.loads(f.read())['root'])

def save(root):
    f = open(savefile, 'w')
    root = {'root': tree_to_map(root)}
    f.write(json.dumps(root))

def start():
    root = load()
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
        response = input('Are you thinking of a %s? ' % guessed_animal)

        # guessed right
        if response is 'y':             
            print('Thanks for playing!')

        # guessed wrongly
        else:                           
            new_animal      = input('Oh dear, what was the right answer? ')
            new_question    = input('What is a question that distinguishes %s from %s? ' % (new_animal, guessed_animal))
            new_animal_response = input('What would the answer be for %s? ' % new_animal)

            # add new question
            new_node = Node(new_question + " ")
            if new_animal_response is 'y':
                new_node.yes    = Node(new_animal)
                new_node.no     = curr
            else:
                new_node.no     = Node(new_animal)
                new_node.yes    = curr

            if prev_response is 'y':
                prev.yes    = new_node
            else:
                prev.no     = new_node

        save(root)

start()
