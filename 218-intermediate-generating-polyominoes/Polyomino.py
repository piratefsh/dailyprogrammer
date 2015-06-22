import numpy as np
import math
import bisect

class Polyomino():
	# Constructs a Polyomino on a canvas that can accomodate max size,
	# which is sixe x size
	def __init__(self, size):
		self.size		= size
		self.tiles 		= 0 # number of tiles added
		self.coords 	= set()
		self.incarnations = None

	# Returns coordinates of all open sides 
	def open_sides(self):
		coords = []
		for c in self.coords:
			# check top, bottom, left, right
			# if has top cell and top doesn't have tile 
			x, y = c[0], c[1]
			if x-1 >= 0 and (x-1,y) not in self.coords:
				coords.append((x-1, y))

			if x+1 < self.size and (x+1,y) not in self.coords:
				coords.append((x+1, y))

			if y-1 >= 0 and (x,y-1) not in self.coords:
				coords.append((x, y-1))

			if y+1 < self.size and (x,y+1) not in self.coords:
				coords.append((x, y+1))
		return coords

	# Adds tile at given coordinates
	def set(self, coords):
		self.tiles += 1
		self.coords.add(coords)
		return self

	# add tiles for given coords
	def set_coords(self, coords):
		for c in coords:
			self.set(c)
		return self

	def identical(self, other):
		return self.coords == other.coords

	# normalize self
	def normalize(self):
		# get smallest x and smallest y
		min_x = int(min(self.coords, key=lambda x: x[0])[0])
		min_y = int(min(self.coords, key=lambda x: x[1])[1])
		normalized_coords = [(c[0]-min_x, c[1]-min_y) for c in self.coords]
		self.set_coords(normalized_coords)
		return self

	def normalized(self):
		# get smallest x and smallest y
		min_x = int(min(self.coords, key=lambda x: x[0])[0])
		min_y = int(min(self.coords, key=lambda x: x[1])[1])
		normalized_coords = [(c[0]-min_x, c[1]-min_y) for c in self.coords]
		p = Polyomino(self.size).set_coords(normalized_coords)
		return p

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
		for c in self.coords:
			mult = rotation * np.matrix("%d;%d" % (c[0],c[1])) 
			rotated_coords.append(mult)
				
		# get lowest values for x and y 
		min_x = int(min(rotated_coords, key=lambda x: x[0][0])[0][0])
		min_y = int(min(rotated_coords, key=lambda x: x[1][0])[1][0])

		# create rotated polyamino
		rotated = Polyomino(self.size)

		# normalize. have to normalize before setting coords as there are negative values
		rotated.set_coords([(int(c[0][0])-min_x, int(c[1][0])-min_y) for c in rotated_coords])
		return rotated

	# Check equality of this poly to another
	def __eq__(self, other):
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

	def __hash__(self):
		return hash(repr(self))

	def __repr__(self):
		string = ""
		grid = [ [False] * self.size for i in range(self.size)]
		for coord in self.coords:
			grid[coord[0]][coord[1]] = True
		for row in grid:
			for cell in row:
				string += '# ' if cell else '. '
			string += "\n"
		return string