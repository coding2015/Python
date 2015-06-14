#!/usr/bin/python
'''
Generate a list of a random number(1<N<=100) of random numbers(0<=n<=2^31-1).
Then randomly select a set of these numbers(1<=N<=100),sort them and display.
'''

import random

def RandomList(l):
	'''
	Generate a list of ranndom number(1<N<=100) of
		random numbers (0 <= n <= 2^31-1).
	'''
	for i in range(random.randint(2,100)):
		l.append(random.randint(0, 2**31-1))
	

def SubRandomList(l):
	'''
	Randomly select a set of numbers from the given list(1 <= N <= len(l))
	sort them,and display this subset.
	'''
	sub = []
	for i in range(random.randint(1,len(l))):
		sub.append(random.choice(l))
	sub.sort()
	return sub


def main():
	l = []
	RandomList(l)
	sub = SubRandomList(l)
	print 'The list[%d]:\n%s' % (len(l),l)
	print ""
	print 'The sublist[%d]:' % len(sub)
	for i in range(len(sub)):
		print sub[i]

#entry
if __name__ == '__main__':
	main()	
