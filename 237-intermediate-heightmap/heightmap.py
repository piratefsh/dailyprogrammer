
"""
Boxes on layer 0 should be filled with the character #;
Boxes on layer 1 should be filled with the character =;
Boxes on layer 2 should be filled with the character -;
Boxes on layer 3 should be filled with the character .;
Boxes on layer 4 and above should not be filled.
"""
char_map = ['#', '=', '-', '.', ' ']

def map_height(boxes):
    boxes = boxes.split('\n')

    mapped = [[0] * len(row) for row in boxes]

    # count and keep number of edges on col
    num_edges = get_num_edges(boxes)
    curr_heights = [-1] * len(boxes[0])
    edge_count = [0] * len(boxes[0])

    for r, row in enumerate(boxes):
        for c, cell in enumerate(row):

            if cell == ' ':
                # mapped[r][c] = char_map[curr_heights[c]]
                mapped[r][c] = str(curr_heights[c])
            if cell == '-':
                edge_count[c] += 1
                if edge_count[c] <= num_edges[c]/2:
                    curr_heights[c] = curr_heights[c] + 1 
                else:
                    curr_heights[c] = curr_heights[c] - 1
                mapped[r][c] = cell
            elif cell == '|' or cell == '+':
                mapped[r][c] = cell
                

    #       if in box, draw symbol based off height
    return mapped

def boxes_repr(boxes):
    outstr = ''
    for row in boxes:
        for col in row:
            outstr += col
        outstr += '\n'
    return outstr[:-1]

def get_num_edges(boxes):
    #for each column, count edges
    num_edges = [0] * len(boxes[0])

    for row in boxes:
        for c, cell in enumerate(row):
            if row[c] == '-':
                num_edges[c] += 1

    return num_edges

def test():
    boxes = None
    expected = None

    # small input

    with open('input01.txt') as f:
        boxes = f.read()
    with open('output01.txt') as f:
        expected = f.read() 

    edges = get_num_edges(boxes.split('\n'))
    assert edges == [0, 2, 2, 4, 2, 2, 0]

    mapped =  map_height(boxes)      
    # assert boxes_repr(mapped) == expected

    # large input

    with open('input00.txt') as f:
        boxes = f.read()
    with open('output00.txt') as f:
        expected = f.read() 
    
    mapped =  map_height(boxes)     

    with open('output00-test.txt', 'w') as f: 
        f.write(boxes_repr(mapped))

    assert boxes_repr(mapped) == expected

    print('tests pass')
