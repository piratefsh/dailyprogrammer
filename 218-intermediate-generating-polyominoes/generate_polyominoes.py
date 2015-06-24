import sys
from Polyomino import Polyomino

def gen(n, size):
    if n == 1:
        return set([Polyomino(size).set((0, 0))])
    else:
        polys = set()
        prev = gen(n-1, size)
        for p in prev:
            for side in p.open_sides():
                new = Polyomino(n).set_coords(p.coords)
                new.set(side)
                polys.add(new)
        return polys

size = int(sys.argv[1])
polys = gen(size, size)
for p in polys:
    print p.normalize()

print(len(polys))




 

