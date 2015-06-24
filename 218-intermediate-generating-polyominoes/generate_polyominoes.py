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
		poly.normalize()
		polys.append(norm)
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
unique = []

find_polyominoes(init, size, polys)

for p in set(polys):
	if p not in unique:
		unique.append(p)
		print(p)

print(len(unique))

