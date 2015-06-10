import sys

def is_palindrome(s):
	if len(s) < 2:
		return True
	return s[0] == s[-1] and is_palindrome(s[1:-1])

input_num 	= sys.argv[1]
num 		= input_num
steps 		= 0

while not is_palindrome(num):
	steps += 1
	num = str(int(num) + int(num[::-1]))

print('%s gets palindromic after %d steps: %s' % (input_num, steps, num))
