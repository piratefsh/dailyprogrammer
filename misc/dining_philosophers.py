import time, logging, sys, random
from threading import Thread, Lock

# Configure logging
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
	eat_time = 1.0
	think_time = 1.0

	def __init__(self, left_fork, right_fork):
		Thread.__init__(self)
		self.id = Philosopher.counter
		self.setName('Philosopher %d' % self.id)
		Philosopher.counter += 1

		# Forks
		self.left = left_fork
		self.right = right_fork

	def run(self):
		""" 
		Think and eat forever
		"""
		for _ in range(5):
			self.get_forks()
			self.eat()
			self.release_forks()
			self.think()

	def get_forks(self):
		"""
		Get forks on right and left of Philosopher if available
		"""
		logging.info('Waiting for fork %d' % self.left.id)
		self.left.pickup()
		logging.info('Picked up fork %d' % self.left.id)
		logging.info('Waiting for fork %d' % self.right.id)
		self.right.pickup()
		logging.info('Picked up fork %d' % self.right.id)

	def eat(self):
		"""
		Spend time eating
		"""
		logging.info(repr(self) + " is eating")
		time.sleep(random.random() * self.eat_time)
		return 

	def release_forks(self):
		"""
		Return forks to their original places
		"""
		if self.left.is_used():
			self.left.putdown()
			logging.info('Released fork %d' % self.left.id)
		if self.right.is_used():
			self.right.putdown()
			logging.info('Released fork %d' % self.right.id)

	def think(self):
		"""
		Spend time thinking
		"""
		logging.info(repr(self) + " is thinking")
		time.sleep(random.random() * self.think_time)
		return

	def __repr__(self):
		return "Philosopher %d" % self.id

class Fork():
	"""
	Fork is a shared resource among Philosophers. A Fork
	can only be held by one Philosopher at a time
	"""
	counter = 0
	timeout = 2 # in seconda

	def __init__(self):
		self.lock = Lock()
		self.id = Fork.counter 
		Fork.counter += 1

	def is_used(self):
		return self.lock.locked()

	def pickup(self):
		start = time.time()
		got_lock = False
		while time.time() - start < self.timeout and not got_lock:
			got_lock = self.lock.acquire(0)
		if not got_lock:
			logging.error('Deadlock')
			exit()

	def putdown(self):
		self.lock.release()

def test():
	num_philos = int(sys.argv[1])
	philosophers = []
	forks = [Fork() for _ in range(num_philos)]

	for i in range(num_philos):
		right_index = 0 if i == num_philos - 1 else i + 1
		p = Philosopher(left_fork=forks[i], right_fork=forks[right_index])
		philosophers.append(p)

	map(lambda x: x.start(), philosophers)

test()