
"""
Boxes on layer 0 should be filled with the character #;
Boxes on layer 1 should be filled with the character =;
Boxes on layer 2 should be filled with the character -;
Boxes on layer 3 should be filled with the character .;
Boxes on layer 4 and above should not be filled.
"""
char_map = ['#', '=', '-', '.', ' ']

def rotate(boxes):
    edge_map = {
        '-' : '|',
        '|' : '-',
        ' ' : ' ',
        '+' : '+'
    }

    rotated = []
    for c, col in enumerate(boxes[0]):
        rot_row = []
        for r, row in enumerate(boxes):
            rot_row.append(edge_map[row[c]])
        rotated.append(rot_row)
    return rotated

def map_height(boxes):
    boxes = boxes.split('\n')
    rotated = rotate(boxes)

    mapped = [[0] * len(row) for row in boxes]

    # count and keep number of edges on col
    num_edges = get_num_edges(boxes)

    curr_heights = [-1] * len(boxes[0])
    edge_count = [0] * len(boxes[0])

    for r, row in enumerate(boxes):
        for c, cell in enumerate(row):
            if cell == ' ':
                mapped[r][c] = char_map[curr_heights[c]]
                # mapped[r][c] = str(curr_heights[c])
            if cell == '-':
                edge_count[c] += 1
                if edge_count[c] <= num_edges[c]/2:
                    curr_heights[c] = curr_heights[c] + 1
                else:
                    curr_heights[c] = curr_heights[c] - 1

                mapped[r][c] = cell
            
            if cell == '|':
                mapped[r][c] = cell

            if cell == '+':
                mapped[r][c] = cell
                
    return mapped

def boxes_repr(boxes):
    outstr = ''
    for row in boxes:
        for col in row:
            outstr += str(col)
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

def get_inout(infile, outfile):
    boxes = None
    expected = None

    with open(infile) as f:
        boxes = f.read()
    with open(outfile) as f:
        expected = f.read() 
    
    return boxes, expected

def write_out(outfile, content):
    with open(outfile, 'w') as f: 
        f.write(content)

def test():
    # small input
    boxes, expected = get_inout('input01.txt', 'output01.txt')

    edges = get_num_edges(boxes.split('\n'))
    assert edges == [0, 2, 2, 4, 2, 2, 0]

    mapped =  map_height(boxes)      
    # assert boxes_repr(mapped) == expected

    # large input
    boxes, expected = get_inout('input02.txt', 'output02.txt')    
    mapped =  map_height(boxes)     

    assert boxes_repr(mapped) == expected
    print('tests pass')

def test_tricky():
    # tricky
    boxes, expected = get_inout('input00.txt', 'output00.txt') 
    out = boxes_repr(map_height(boxes))
    write_out('output00-test.txt', out)

    assert out == expected

    print('tests pass')
