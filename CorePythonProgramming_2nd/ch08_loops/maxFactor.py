#!/usr/bin/python

'''
Example 8.1:
	This program displays the largest factors of numbers between 10 and 20.
	If the number is prime, the script will indicate that as well.

KeyPoint: 
	while-else
'''

def showMaxFactor(num):
	count = num/2 #!good idea: it reduces half of the work to find
	while count > 1:
		if num % count == 0:
			print "%d's largest factor is %d" % \
				(num, count)
			break
		count -= 1
	else:
		print num, 'is prime'


for eachNum in range(10,21):
	showMaxFactor(eachNum)
