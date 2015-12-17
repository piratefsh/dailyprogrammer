import sys
digits = list(map(int, list(sys.argv[1])))
cycles = []
stop = False
while not stop:
	curr = sum([int(x)**2 for x in digits])

	try:
		cycles.index(curr)
		stop = True
		break
	except ValueError:
		cycles.append(curr)

	digits = list(str(curr))


print(cycles)