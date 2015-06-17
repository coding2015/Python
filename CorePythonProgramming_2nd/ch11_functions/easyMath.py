#!/usr/bin/python
'''
Example 11.1
	Randomly chooses numbers and an arithmetic function, 
	displays the question, and verifies the result.
	Shows answer after three wrong tries and does not continue
	until the user enters the correct answer
'''

from operator import add, sub, mul, div
from random import randint, choice

ops = {'+':add, '-':sub, '*':mul, '/':div}
MAXTRIES = 2 #it should be 2 instead of 3
			 #according to the requirement, once three-times are wrong 
			 #it will show the answer, which means it shows answer as soon as
			 #the third time incorrect, ie. the former value of oops is 2, 

def doprob():
	op = choice('+-*/')	
	nums = [randint(1,100) for i in range(2)] #produce two integers in [1,100]
	nums.sort(reverse = True) #make nums[0] > nums[1]
	ans = ops[op](*nums) #record the standard answer
						#'*' means take the (list/tuble)'s elements as args
						#len(list/tuble) must equal to args'number
	expr = '%d %s %d = ' % (nums[0], op, nums[1])
	oops = 0
	while True:
		try:
			if int(raw_input(expr)) == ans:
				print 'correct'
				break
			else:
				if oops == MAXTRIES:
					print 'sorry... the answer is\n%s%d' % (expr, ans)
				else:
					print 'incorrect... try again'
					oops += 1  # !once oops == MaxTries, it will never increase!
		except (KeyboardInterrupt, EOFError, ValueError):
				print 'invalid input... try again'


def main():
	while True:
		doprob()
		try:
			opt = raw_input('Again? [Y]').lower()
			if opt and opt == 'n':
				break
		except (KeyboardInterrupt, EOFError):
			break


if __name__ == '__main__':
	main()
			

