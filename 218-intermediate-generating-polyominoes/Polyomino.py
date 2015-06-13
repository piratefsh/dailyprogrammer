class Polyomino():
	def __init__(self, size):
		self.grid = [ [False] * size for i in range(size)]
		self.last_added = [None, None]

	# Returns coordinates of open sides 
	# (adjacent sides with no set tiles) of self.last_added coords
	def open_sides_of_last_added(self):
		coords = []
		g = self.grid
		x = self.last_added[0]
		y = self.last_added[1]
		
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

	def set(self, coords):
		self.grid[coords[0]][coords[1]] = True
		self.last_added = coords
		return self

	def __repr__(self):
		string = ""
		for row in self.grid:
			for cell in row:
				string += '# ' if cell else '. '
			string += "\n"
		return string