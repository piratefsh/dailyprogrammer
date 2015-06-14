import sys
from Polyomino import Polyomino
from copy import deepcopy

size = int(sys.argv[1])
center = size/2-1
init = Polyomino(size).set((center, center))

def find_polyominoes(poly, tiles_left, polys):
	# if no more tiles left to add, return
	if tiles_left == 1:
		# add to array
		if poly not in polys:
			polys.append(poly)
		return
	# else, if still have tiles
	else:
		# decrement tiles
		tiles_left -= 1
		# for each open side of last added tile,
		for side in poly.open_sides():
			# duplicate current poly add new tile at side
			p = deepcopy(poly)
			p.set(side)
			# find more polyominoes with new polyomino and add those to array
			find_polyominoes(p, tiles_left, polys)

polys = []
find_polyominoes(init, size, polys)

for p in polys:
	print(p)

print(len(polys))

# test_case = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (3, 1)]
# test_case = [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)]
# test_case = [(0, 1), (1, 1), (2, 0), (2, 1), (3, 0), (4, 0)]
# test_case = [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)]
# t = Polyomino(size)
# for c in test_case:
# 	t.set(c)

#print(t)

# for p in polys:
# 	if p == t:
# 		print(p)

