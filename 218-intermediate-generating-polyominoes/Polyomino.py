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
		self.coords = set(coords)
		self.tiles = len(coords)
		return self

	def identical(self, other):
		return self.coords == other.coords

	def normalized_coords(self):
		# get smallest x and smallest y
		min_x = min(self.coords, key=lambda x: x[0])[0]
		min_y = min(self.coords, key=lambda x: x[1])[1]
		return [(c[0]-min_x, c[1]-min_y) for c in self.coords]

	# normalize self
	def normalize(self):
		self.set_coords(self.normalized_coords())
		return self

	def normalized(self):
		normalized_coords = self.normalized_coords()
		p = Polyomino(self.size).set_coords(normalized_coords)
		return p

	# get reflection of self
	def reflections(self):
		p = Polyomino(self.size).set_coords([(c[1], c[0]) for c in self.coords])
		return [p]
		
	# get possible rotations of self
	def rotations(self):
		return [self.rotate(1), self.rotate(2), self.rotate(3)]
		
	# get a given rotation of self
	def rotate(self, num_times):
		# get rotated coords
		rotated_coords = self.coords
		for _ in range(num_times):
			rotated_coords = [(-y,x) for x,y in rotated_coords]
		
		# create rotated polyamino
		return Polyomino(self.size).set_coords(rotated_coords).normalize()

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
		for x in grid:
			for y in row:
				string += '# ' if (x,y) in self.coords else '. '
			string += "\n"
		return string