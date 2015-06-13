import sys
from Polyomino import Polyomino
from copy import deepcopy

size = int(sys.argv[1])
init = Polyomino(size).set((0, 0))

def find_polyominoes(poly, tiles_left, polys):
	# if no more tiles left to add, return
	if tiles_left == 1:
		return

	# else, if still have tiles
	else:
		# decrement tiles
		tiles_left -= 1

		# for each open side of last added tile,
		for side in poly.open_sides_of_last_added():
			# duplicate current poly add new tile at side
			p = deepcopy(poly)
			p.set(side)

			# add to array
			polys.append(p)

			# find more polyominoes with new polyomino and add those to array
			find_polyominoes(p, tiles_left, polys)


polys = []
find_polyominoes(init, size, polys)

for p in polys:
	print(p)
