import sys
from Polyomino import Polyomino
from copy import deepcopy

size = int(sys.argv[1])
init = Polyomino(size).set((0, 0))

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

print(len(polys))

print("--------------------------")

def remove_dupes(polys):
	clean = []
	for p in polys:
		if p not in clean:
			clean.append(p)
	return clean
polys = remove_dupes(polys)

for p in polys:
	print(p)
print(len(polys))
