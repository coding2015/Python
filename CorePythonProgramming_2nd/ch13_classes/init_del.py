#!usr/bin/python


class P(object):
	def __init__(self):
		print 'P init'
	
	def __del__(self):
		print 'P del'


class C(P):
	def __init__(self):
		print 'C init'
	
	def __del__(self):
		P.__del__(self)  # 1
		print 'C del'


mc = C()
mv = mk = mc



print '1:',
del mc
print '2:',
del mk
print '3:',
del mv

print 'end'

while True:
	pass


# Result
# 0
'''
C init
1: 2: 3: C del
end

'''
# 1
'''
C init
1: 2: 3: P del
C del
end

'''

