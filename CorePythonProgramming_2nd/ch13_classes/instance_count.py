#!usr/bin/python

class InstCt(object):
	count = 0

	def __init__(self):
		# count += 1 # Error
		#UnboundLocalError: local variable 'count' referenced before assignment
		InstCt.count += 1

	def __del__(self):
		InstCt.count -= 1


a = InstCt()
print InstCt.count
c=b=a
print InstCt.count
del b
print InstCt.count
del c
print InstCt.count
del a
print InstCt.count



# result
'''
1
1
1
1
0
'''
