#!/usr/bin/python

'''
Exercise 8-11:
	first require the user to give the total number of names
	required name's formate: last name,first name, ie:','is necessary
	if the formate is incorrect:
			inform the user to correct 
			show the error-times
	in the end, show the name list sorted by last name
'''

names = []

num = int(raw_input('Enter total number of names: '))
i = 1

errMsg = """
Wrong format, name's format should be: Last, First
You have done this %d time(s) already.Fixing input...
"""
errTimes = 0

while i <= num:
	prompt = 'Please enter name %d: ' % i
	name = raw_input(prompt)	
	if ',' not in name:
		errTimes += 1
		print errMsg % errTimes
	else:
		names.append(name)
		i += 1

print
print 'The sorted list (by last name) is:'
for name in sorted(names):
	print ' '*5, name

