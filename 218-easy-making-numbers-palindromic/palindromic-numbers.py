import sys

input_num 	= sys.argv[1]
num 		= input_num
steps 		= 0

while not num == num[::-1]:
	steps += 1
	num = str(int(num) + int(num[::-1]))

print('%s gets palindromic after %d steps: %s' % (input_num, steps, num))
