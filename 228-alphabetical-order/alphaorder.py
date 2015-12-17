import sys 

def in_order(word):
	return "".join(sorted(list(word))) == word

def reversed(word):
	return in_order(word[::-1])

for word in sys.stdin:
	word = word.strip()
	if in_order(word):
		print word, 'IN ORDER'
	elif reversed(word):
		print word, 'REVERSED'
	else:
		print word, 'NOT IN ORDER'
