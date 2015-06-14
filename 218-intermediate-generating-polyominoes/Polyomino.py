import numpy as np
import math

class Polyomino():
	# Constructs a Polyomino on a canvas that can accomodate max size,
	# which is sixe x size
	def __init__(self, size):
		self.size		= size
		self.grid 		= [ [False] * size for i in range(size)]
		self.tiles 		= 0 # number of tiles added
		self.coords 	= []
		self.incarnations = None

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
		self.tiles += 1
		self.coords.append(coords)
		return self

	# add tiles for given coords
	def set_coords(self, coords):
		for c in coords:
			self.set(c)
		return self

	def identical(self, other):
		# Check if straight out identical 
		same = True
		for x,row in enumerate(self.grid):
			for y,cell in enumerate(row):
				if self.grid[x][y] is not other.grid[x][y]:
					same = False
		return same

	# normalize self
	def normalize(self):
		# # get smallest x and smallest y
		min_x = int(min(self.coords, key=lambda x: x[0])[0])
		min_y = int(min(self.coords, key=lambda x: x[1])[1])
		self.coords = [(c[0]-min_x, c[1]-min_y) for c in self.coords]
		for x,row in enumerate(self.grid):
			for y,cell in enumerate(row):
				self.grid[x][y] = True if (x, y) in self.coords else False
		return self

	# get reflection of self
	def reflections(self):
		p = Polyomino(self.size).set_coords([(c[1], c[0]) for c in self.coords])
		return [p]
		
	# get possible rotations of self
	def rotations(self):
		rot90	= np.matrix("0, -1; 1, 0")
		rot180	= np.matrix("-1, 0; 0, -1")
		rot270	= np.matrix("0, 1; -1, 0")
		return [self.rotate(rot90), self.rotate(rot180), self.rotate(rot270)]
		
	# get a given rotation of self
	def rotate(self, rotation):
		# get rotated coords
		rotated_coords = []
		for x,row in enumerate(self.grid):
			for y,cell in enumerate(row):
				if self.grid[x][y]:
					mult = rotation * np.matrix("%d;%d" % (x,y)) 
					rotated_coords.append(mult)
				
		# get lowest values for x and y 
		min_x = int(min(rotated_coords, key=lambda x: x[0][0])[0][0])
		min_y = int(min(rotated_coords, key=lambda x: x[1][0])[1][0])

		# create rotated polyamino
		rotated = Polyomino(self.size)

		# normalize. have to normalize before setting coords as there are negative values
		for coord in rotated_coords:
			coord[0][0] += -min_x
			coord[1][0] += -min_y
			rotated.set((coord[0][0], coord[1][0]))
		return rotated

	# Check equality of this poly to another
	def __eq__(self, other):
		# Normalize both
		self.normalize()
		other.normalize()
		
		# Create and store possible incarnations of self
		if self.incarnations is None:
			reflections 		= self.reflections()
			rotated_reflections = sum(map(lambda x: x.rotations(), reflections), [])
			self.incarnations 	= [self] + self.reflections() + self.rotations() + rotated_reflections

		# Check other against possible incarnations
		for inc in self.incarnations:
			if other.identical(inc):
				return True

		return False

	# Print out this polyomino
	def __repr__(self):
		string = ""
		for row in self.grid:
			for cell in row:
				string += '# ' if cell else '. '
			string += "\n"
		return string