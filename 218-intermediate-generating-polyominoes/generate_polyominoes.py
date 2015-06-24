import sys
from Polyomino import Polyomino

def gen(n, size):
    if n == 1:
        center = size/2
        return [Polyomino(size).set((center, center))]
    else:
        polys = []
        prev = gen(n-1, size)
        for p in prev:
            enlarge = Polyomino(n).set_coords(p.coords)
            for side in enlarge.open_sides():
                new = Polyomino(n).set_coords(p.coords)
                new.set(side)
                if new not in polys:
                    polys.append(new)
        return polys

size = int(sys.argv[1])
polys = gen(size, size)
for p in polys:
    print p.normalize()

print(len(polys))




 

