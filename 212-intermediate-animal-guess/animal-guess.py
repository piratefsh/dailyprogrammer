from pprint import pprint
savefile = 'animals.txt'

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
    def hasNext(self):
        return self.yes or self.no
    def __repr__(self):
        return self.content

# returns tree as a string recursively
def tree_to_string(root, count=0):
    curr = root
    if not curr:
        return ""
    left    = tree_to_string(curr.yes, count + 1)
    right   = tree_to_string(curr.no, count + 1)
    left    = "\n" + left.strip() if len(left) > 0 else left
    right   = "\n" + right.strip() if len(right) > 0 else right
    padding = ""
    for i in range(count):
        padding += "-"
    return padding + curr.content.strip() + left + right

def tree_as_array(curr, arr=[], index=0):
    if not curr:
        return arr
    arr.insert(index, curr)
    tree_as_array(curr.yes, arr, (index+1)*2-1)
    tree_as_array(curr.no, arr, (index+1)*2)

    return arr

def array_to_tree(arr, index=0):
    if index >= len(arr) or arr[index] is '\n':
        return None
    tree = Node(arr[index])
    tree.yes = array_to_tree(arr, (index+1)*2-1)
    tree.no = array_to_tree(arr, (index+1)*2)
    return tree

def load(file):
    f = open(savefile, 'r')
    arr = f.readlines()
    tree = array_to_tree(arr)
    return tree

def save(arr):
    f = open(savefile, 'w')
    for node in arr:
        line = node.content if node else ""
        f.write(line.strip() + "\n")
    f.close()

def start():
    root = load(savefile)
    while True:
        print(tree_to_string(root))
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

        save(tree_as_array(root))

start()