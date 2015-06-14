#!/usr/bin/python
'''
This simple script uses list as a stack 
to store and retrieve strings entered through this menu-driven text application
using only the append() and pop() list methods.
'''
stack = []

def pushit():
	stack.append(raw_input('Enter new string:\n> ').strip())

def popit():
	if len(stack) == 0:
		print 'Cannot pop from an empty stack!'
	else:
		print 'Removed [',repr(stack.pop()),']'

def viewstack():
	print stack

CMDs = {'u':pushit, 'o':popit, 'v':viewstack}

def showmenu():
	pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice:"""

	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except (EOFError, KeyboardInterrupt, IndexError):
				choice = 'q'
	
			print '\n You picked:[%s]' % choice
			if choice not in 'uovq':
				print 'Invalid option,try again'
			else:
				break

		if choice == 'q':
			break
		CMDs[choice]()

if __name__ == '__main__':
	showmenu()		
