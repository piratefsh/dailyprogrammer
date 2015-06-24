import sys
from Polyomino import Polyomino

def gen(n, size):
    if n == 1:
        return [Polyomino(size).set((0, 0))]
    else:
        polys = []
        prev = gen(n-1, size)
        for p in prev:
            for side in p.open_sides():
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




 

