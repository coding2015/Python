#!/usr/bin/python
'''
use list as queue
use list methods: append(obj) and pop(index) 
'''

queue = []

def enQ():
	queue.append(raw_input('enter new string> ').strip())

def deQ():
	if len(queue) == 0:
		print 'Cannot pop from an empty queque.'
	else:
		print 'removed [',`queue.pop(0)`,']'

def viewQ():
	print queue

CMDs = {'e':enQ,'d':deQ,'v':viewQ}

def showMenu():
	pr = '''
(E)nterQ
(D)eleteQ
(V)iewQ
(Q)uit

Enter choice: '''

	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except (EOFError, KeyboardInterrupt, IndexError):
				choice = 'q'			

			print '\nYou picked:[%s]' % choice
			if choice not in 'edvq':
				print 'Invalid choice,try again.'
			else:
				break
		
		if choice == 'q':
			break
		else:
			CMDs[choice]()

if __name__ == '__main__':
	showMenu()

