char_map = ['#', '=', '-', '.']


def flood(grid, node, target, depth):
    x, y = node

    color = char_map[depth] if depth < len(char_map) else None
    
    if target == color:
        return

    if node not in grid or str(grid[node]) not in target:
        return 

    if grid[node] in '+|-':
        flood(grid, (x+1, y+1), target, depth+1)

    if grid[node] == ' ':
        grid[node] = color 
        flood(grid, (x+1, y), target, depth)
        flood(grid, (x, y+1), target, depth)
        flood(grid, (x-1, y), target, depth)
        flood(grid, (x, y-1), target, depth)

    return

def grid_repr(grid):
    outstr = ''
    for x,y in sorted(grid.keys()):
        if y == 0 and x != 0:
            outstr += '\n'
        outstr += grid[(x, y)] if grid[(x, y)] is not None else ' '
    return outstr

def get_inout(infile, outfile):
    boxes = None
    expected = None

    with open(infile) as f:
        boxes = f.read()
    with open(outfile) as f:
        expected = f.read() 
    
    return boxes, expected


def test_flood_one(inf, outf):
    # tricky
    boxes, expected = get_inout(inf, outf) 
    
    grid = {}

    for r, row in enumerate(boxes.split('\n')):
        for c, char in enumerate(row):
            grid[(r, c)] = char 

    flood(grid, (0, 0), ' +=|', -1)
    out = grid_repr(grid)
    print(out)
    assert out == expected
    print('tests pass')

def test():
    test_flood_one('input00.txt', 'output00.txt')
    test_flood_one('input02.txt', 'output02.txt')
    test_flood_one('input03.txt', 'output03.txt')

