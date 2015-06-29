#!/usr/bin/python
#coding:utf-8

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

def move(a,c,n):
	print '%d:%c-->%c' % (n, a, c)
	global moves  #!neccessary to declare before assignment
				  	# otherwise it will produce UnbondLocalError
					# because of conflict between global and local vals
	moves += 1

#def hanoi(a='A',b='B',c='C',n): #递归函数的参数不能设置默认值
def hanoi(a, b, c, n):
	"move n plates from A seat to C seat by B seat"
	if n>1:
		hanoi(a,c,b,n-1)
		move(a,c,n)
		hanoi(b,a,c,n-1)
	else:
		move(a,c,n)


def main():
	n = int(raw_input('enter the total number of plates> '))
	hanoi('A','B','C',n)
	print 'moves:',moves

if __name__ == '__main__':
	main()
