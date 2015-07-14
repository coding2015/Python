#!/usr/bin/python
#coding:utf-8

'''
Exercise 7-14 plus
'''

from random import randint

def genSet():
	'produce a set contains 1~10 numbers in [0,9]'
	return set(randint(0,9) for i in range(randint(1,10)))

def potentialSubSet(s):
	'produce a set which is potential to be the subset of the given set'
	return set(randint(0,9) for i in range(randint(0, len(s))))
						# 注意当range(0)为[], 此时返回空集，空集是任一集合的子集

def main():
	A = genSet()
	B = potentialSubSet(A)
	print 'A:', A
	print 'B:', B

	result = B<=A	
	DONE = False	# 记录答对与否
	MAX = 3		# 给MAX次机会

	while MAX:
		MAX -= 1
		judge = raw_input('B is sub to A?(Yes/No)> ')
		r = True if judge[0].lower()=='y' else False
	
		if r == result:
			print 'Good job!'
			DONE = True
			break
		print 'Oop! not the right answer!' 

	if not DONE:
		print 'The right answers are:'
		print 'B is sub to A:', result


if __name__ == '__main__':
	main()


'''
$ python random_set3.py 
A: set([0, 1, 4, 5, 6, 7])
B: set([0, 1, 4, 5, 6])
B is sub to A?(Yes/No)> n
Oop! not the right answer!
B is sub to A?(Yes/No)> n
Oop! not the right answer!
B is sub to A?(Yes/No)> n
Oop! not the right answer!
The right answers are:
B is sub to A: True
'''
