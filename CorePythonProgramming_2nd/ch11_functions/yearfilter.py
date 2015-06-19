#!/usr/bin.python

'''
Exercise 11-8:
	given a years' list and return a leap years' list

KeyPoint:
	BIF:filter()
	line comprehension

Problem:
	priority combination of 'not and or' 
Test-Conlude:
	not > and/or: it combine from left to right
'''

# filter() 
import sys
sys.path.append('/home/megan/Githubs/Python/CorePythonProgramming_2nd/ch05_numbers')
from leapyear import isleapyear

def yearsfilter(years):
	leaps = filter(isleapyear,years)
	return leaps

#years = [1999, 2000, 432, 2014, 2016]
#print 'years:', years
#print 'leaps:', yearsfilter(years)
#
#
## line comprehension
#print 'line comprehension:\nleaps:', [y for y in years \
#		if ( y % 4 == 0 and y % 100) or y % 400 == 0] 
#


years = range(-2000,3000)
lf = yearsfilter(years) 
ll = [y for y in years if not y%4 and y%100 or not y%400 ]
			# same as: if (y % 4 == 0 and y % 100) or y % 400 == 0
print 'len:',len(lf) ,len(ll)  #len(ll)> len(lf)
for y in ll:
	if y not in lf:
		print y

