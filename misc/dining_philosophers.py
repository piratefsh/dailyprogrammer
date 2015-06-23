import time
import logging
from threading import Thread
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
logging.getLogger().setLevel(logging.INFO)


class Philosopher(Thread):
	"""
	Philosopher instance runs in their own thread. 
	A Philosopher does the following indefinitely:
	1. Pick up right fork and left fork if are available
	2. Eat spaghetti
	3. Put down forks
	4. Think
	"""

	counter = 0
	eat_time = 1
	think_time = 0.5

	def __init__(self):
		Thread.__init__(self)
		self.id = Philosopher.counter
		self.setName('Philosopher %d' % self.id)
		Philosopher.counter += 1


	def run(self):
		""" 
		Think and eat forever
		"""
		for _ in range(10):
			self.get_forks()
			self.eat()
			self.release_forks()
			self.think()

	def get_forks(self):
		"""
		Get forks on right and left of Philosopher if available
		"""
		return 

	def eat(self):
		"""
		Spend time eating
		"""
		logging.info(repr(self) + " is eating")
		time.sleep(self.eat_time)
		return 

	def release_forks(self):
		"""
		Return forks to their original places
		"""
		return 

	def think(self):
		"""
		Spend time thinking
		"""
		logging.info(repr(self) + " is thinking")
		time.sleep(self.think_time)
		return

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

def test():
	philos = [Philosopher(), Philosopher()]
	map(lambda x: x.start() and x.join(), philos)

test()