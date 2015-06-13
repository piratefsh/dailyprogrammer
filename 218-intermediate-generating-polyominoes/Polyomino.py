import numpy as np
import math

class Polyomino():
	# Constructs a Polyomino on a canvas that can accomodate max size,
	# which is sixe x size
	def __init__(self, size):
		self.size		= size
		self.grid 		= [ [False] * size for i in range(size)]
		self.last_added = (None, None) # coordinates of last tile that was set 
		self.tiles 		= 0 # number of tiles added

	# Returns coordinates of all open sides 
	def open_sides(self):
		coords = []
		g = self.grid

		for x,row in enumerate(self.grid):
			for y,cell in enumerate(row):	
				if self.grid[x][y]:	
					# check top, bottom, left, right
					# if has top cell and top doesn't have tile 
					if x-1 >= 0 and not g[x-1][y]:
						coords.append((x-1, y))

					if x+1 < len(g) and not g[x+1][y]:
						coords.append((x+1, y))

					if y-1 >= 0 and not g[x][y-1]:
						coords.append((x, y-1))

					if y+1 < len(g[x]) and not g[x][y+1]:
						coords.append((x, y+1))
		return coords

	# Adds tile at given coordinates
	def set(self, coords):
		self.grid[coords[0]][coords[1]] = True
		self.last_added = coords
		self.tiles += 1
		return self

	def identical(self, other):
		# Check if straight out identical
		same = True
		for x,row in enumerate(self.grid):
			for y,cell in enumerate(row):
				if self.grid[x][y] is not other.grid[x][y]:
					same = False
		return same

	def get_coords(self):
		coords = []
		for x,row in enumerate(self.grid):
			for y,cell in enumerate(row):
				if self.grid[x][y]:
					coords.append((x, y))
		return coords

	def reflected(self, other):
		# for each this(x,y), other(y,x) has the same value
		for x,row in enumerate(self.grid):
			for y,cell in enumerate(row):
				if self.grid[x][y] is not other.grid[y][x]:
					return False
		return True
		
	def rotated_all(self, other):
		rot90	= np.matrix("0, -1; 1, 0")
		rot180	= np.matrix("-1, 0; 0, -1")
		rot270	= np.matrix("0, 1; -1, 0")
		res = self.rotated(other, rot90) or self.rotated(other, rot180) or self.rotated(other, rot270)
		return res
		
	def rotated(self, other, rotation):
		# get rotated coords
		rotated_coords = []
		for x,row in enumerate(other.grid):
			for y,cell in enumerate(row):
				if other.grid[x][y]:
					mult = rotation * np.matrix("%d;%d" % (x,y)) 
					rotated_coords.append(mult)
				
		# get lowest negative values for x and y 
		min_x = int(math.fabs(int(min(rotated_coords, key=lambda x: x[0][0])[0][0])))
		min_y = int(math.fabs(int(min(rotated_coords, key=lambda x: x[1][0])[1][0])))

		# create rotated polyamino
		rotated = Polyomino(other.size)

		# normalize
		for coord in rotated_coords:
			coord[0][0] += min_x
			coord[1][0] += min_y
			rotated.set((coord[0][0], coord[1][0]))
			
		overlap = [coord_self for coord_self in self.get_coords() if coord_self in rotated.get_coords()]
		
		return len(overlap) == len(rotated.get_coords()) or self.reflected(rotated)

	# Check equality of this poly to another
	def __eq__(self, other):
		# Check all possible transformations
		return self.identical(other) or self.rotated_all(other) or self.reflected(other) 

	# Print out this polyomino
	def __repr__(self):
		string = ""
		for row in self.grid:
			for cell in row:
				string += '# ' if cell else '. '
			string += "\n"
		return string