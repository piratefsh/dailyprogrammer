import itertools

def run():
	occurs = map(int, raw_input().split(' '))
	print total(occurs)


def total(occurs):
	nums = '4' * occurs[0] + '5' * occurs[1] + '6' * occurs[2]
	combos = (int("".join(n)) 
				for i in range(len(nums))
				for n in itertools.permutations(nums, i + 1))

	return sum(set(combos))

def test():
	assert total([2, 0, 0]) == 4 + 44
	assert total([1, 0, 0]) == 4
	assert total([0, 1, 0]) == 5
	assert total([1, 1, 0]) == 4 + 5 + 45 + 54
	assert total([1, 1, 1]) == 3675
	assert total([1, 2, 3]) == 39345806

run()