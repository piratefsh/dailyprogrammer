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
		polys.append(poly.normalized())
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

cleared = []
for p in polys:
	if p not in cleared:
		cleared.append(p)

for c in cleared:
	print c

print(len(cleared))
