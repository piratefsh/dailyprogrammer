class Philosopher():
	"""
	Philosopher instance runs in their own thread. 
	A Philosopher does the following indefinitely:
	1. Pick up right fork and left fork if are available
	2. Eat spaghetti
	3. Put down forks
	4. Think
	"""

	counter = 0

	def __init__(self):
		self.id = Philosopher.counter
		Philosopher.counter += 1

	def __repr__(self):
		return "Philosopher %d" % self.id

class Fork():
	"""
	Fork is a shared resource among Philosophers. A Fork
	can only be held by one Philosopher at a time
	"""

class Table():
	"""
	Table contains 5 Philosophers and 5 forks between them
	"""

	print [Philosopher(), Philosopher(), Philosopher()]