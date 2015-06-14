#!/usr/bin/python

#def functions:
def Summary(x):
	r = 0
	for e in x:
		r += e
	return r

def Average(x):
	r = Summary(x)
	return (r/len(x))

def List(x):
	for i,e in enumerate(x):
		print "(%d)%d" % (i,e)

def EvenCount(x):
	count = 0
	for i,e in enumerate(x):
		if e%2 == 0 :
			count += 1
			print 'even num:(%d)%d' % (i,e)
	return count


#start
print 'please enter numbers:'
l = [0,0,0,0,0] #need to define numbers of elements
for i in range(5):
	l[i] = int(raw_input('enter a number> '))
print 'You have entered 5 numbers:',l

while True:
	print '''
		Menu
	1.Summary
	2.Average
	3.List
	4.Even Count
	5.Quit
	
	please enter a serial number[1,5]:
	'''
	order = int(raw_input('> '))
	if 1 == order:
		print Summary(l)
	elif 2 == order:
		print Average(l)
	elif 3 == order:
		List(l)
	elif 4 == order:
		print EvenCount(l)
	else:
		break;


