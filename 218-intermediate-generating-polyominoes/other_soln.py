import sys
nmax = int(sys.argv[1])

cell0 = 0, 0  # The cell at (0, 0)
poly1 = (cell0,)  # The 1-polyomino consisting only of cell0

# are the cells adjacent?
def adj(cell1, cell2):
    (x1, y1), (x2, y2) = cell1, cell2
    return abs(x1 - x2) + abs(y1 - y2) == 1

# is the cell connected to the polyomino?
def connected(cell, poly):
    return cell not in poly and any(adj(cell, pcell) for pcell in poly)

# all cells that are connected to this polyomino
def connectedcells(poly):
    xs, ys = zip(*poly)
    xmin, ymin = min(xs) - 1, min(ys) - 1
    xmax, ymax = max(xs) + 1, max(ys) + 1
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            cell = x, y
            if connected(cell, poly):
                yield cell

# the polyomino moved to origin and cells sorted
def normalize(poly):
    xs, ys = zip(*poly)
    x0, y0 = min(xs), min(ys)
    return tuple(sorted((x - x0, y - y0) for x, y in poly))

def reflect(poly):
    return tuple((-x, y) for x, y in poly)
def rotate(poly):
    return tuple((y, -x) for x, y in poly)
# All possible rotations and reflections of this polyomino (normalized)
def versions(poly):
    for j in range(4):
        yield normalize(poly)
        yield normalize(reflect(poly))
        poly = rotate(poly)

# The minimal rotation or reflection of the given polyomino. Any two polyominoes that
# are rotations/reflections of each other should canonicalize to the same value.
def canonical(poly):
    return min(versions(poly))

# every (n+1)-polyomino that can be made by adding a cell to the given n-polyomino
def additions(poly):
    for cell in connectedcells(poly):
        npoly = poly + (cell,)
        yield canonical(npoly)

def printpoly(poly):
    xs, ys = zip(*poly)
    for y in range(max(ys) + 1):
        chars = ["#" if (x, y) in poly else " " for x in range(max(xs) + 1)]
        print("".join(chars))

def polys(n):
    if n == 1:
        return [poly1]
    npolys = set()
    for poly in polys(n - 1):
        for npoly in additions(poly):
            npolys.add(npoly)
    return sorted(npolys)

for poly in polys(nmax):
    printpoly(poly)
    print(" ")