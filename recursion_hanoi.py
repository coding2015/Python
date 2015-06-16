#!/usr/bin/python

'''
hanoi question:
	move n plates from A seat to C seat by B seat
	method:
		1. move n-1 plates from A to B by C
		2. move the N plate from A to C
		3. move n-1 plates from B to C by A
	this function showed the method process by recursion
'''
moves = 0

def Move(a,c,n):
	print '%d:%c-->%c' % (n, a, c)
	global moves  #!neccessary to declare before assignment
				  	# otherwise it will produce UnbondLocalError
					# because of conflict between global and local vals
	moves += 1

def Hanoi(a,b,c,n):
	if n>1:
		Hanoi(a,c,b,n-1)
		Move(a,c,n)
		Hanoi(b,a,c,n-1)
	else:
		Move(a,c,n)


def main():
	n = int(raw_input('enter the total number of plates> '))
	Hanoi('A','B','C',n)
	print 'moves:',moves

if __name__ == '__main__':
	main()
