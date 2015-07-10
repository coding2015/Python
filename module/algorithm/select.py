#!/usr/bin/python

'''
select algorithm:	
	to a position of an array: 
		compare the position's obj with the backward positions' objs
		record the bigger/smaller obj's position
		in the end if the recorded position not equal to the current position
		swap the current position's obj and the recorded position's obj
	there are len(array) times selection
		and during every selection, there are K-1 times compare
		and N-1+N-2+...+1 times compare in tatol
		and 0 to N-1 times exchange
	so the time complextion is: 0(n^2), same as bubble algorithm
'''

def select(a, reverse=False):
	N = len(a)
	if not reverse:
		for i in range(N):
			Min = i		#record the smaller obj's position
			for j in range(i+1,N):
				if a[j] < a[Min]:
					Min = j

			if Min != i:
				a[Min], a[i] = a[i], a[Min]
	else:
		for i in range(N-1):
			Max = i
			for j in range(i,N):
				if a[j] > a[Max]:
					Max = j
			if Max != i:
				a[Max], a[i] = a[i], a[Max]
	return a
	
def test():
	l = [8,7,5,9,3,2,4,6,1]
	print 'before sort:\n',l
	select(l)
	print 'ascending sorted:\n', l
	select(l,True)
	print 'descending sorted:\n',l
	

if __name__ == '__main__':
	test()
