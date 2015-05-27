import itertools, sys
infile 		= open(sys.argv[1])
lines 		= infile.read().split('\n')
comparators = [[int(i) for i in c.split()] for c in lines[1:]]
wires 		= int(lines[0].split()[0])
tests		= itertools.product([0,1], repeat=wires)
for test in tests:
	test = list(test)
	for [left, right] in comparators:
		if test[left] > test[right]:
			test[left], test[right] = test[right], test[left]
	if sorted(test) != test:
		print('Invalid Network')
		exit()

print('Valid')