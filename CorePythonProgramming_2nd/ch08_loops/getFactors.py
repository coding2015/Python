#!/usr/bin/python

'''
Exercise 8-5:
	get all the factors of a given integer
'''

def getFactors(num):
	facts = [num]

# while
#	count = num/2
#	while count >= 1:
#		if num % count == 0:
#			facts.append(count)
#		count -= 1

# for
	for count in range(num/2, 0, -1):
		if num % count == 0:
			facts.append(count)
	
	return facts


num = int(raw_input('enter an integer> '))
facts = getFactors(num)
print "the factors of %d are:" % num
print facts
