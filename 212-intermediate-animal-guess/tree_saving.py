# Various playground methods

from pprint import pprint
from animal_guess import Node
import json

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

    print(curr.content)

    curr.yes = map_to_tree(node["yes"]) if "yes" in node else None
    curr.no = map_to_tree(node["no"]) if "no" in node else None
    return curr

f = open('animals.json', 'r')
tree = json.loads(f.read())['root']

root = map_to_tree(tree)

pprint(json.dumps(tree_to_map(root)))
