#!/usr/bin/python
#coding:utf-8
'''
Study BIF:
	reduce(func, seq[,initial])
	
	initial:
		 初始值，可选变量，不能通过关键字赋值，传入时通过','与*seq区分
		 若seq为空，且initial给定，则直接返回初始值，否则报错
	若列表(包括初始参数)只有一个元素，则不调用func, 直接返回该值
	eg:
		reduce(add, (1,2,3)，0)
'''		


print '---------without init----------'

def my_add(x,y):
	print 'call:my_add(%s,%s)' % (x,y)
	return x + y

def my_sum(*seq):
	print 'my_sum(%s)' % `seq`
	try:
		ret = reduce(my_add, seq)
	except TypeError, diag:
		ret = 'TypeError:'+ str(diag)
	return ret

print my_sum(1,2)	# 调用my_add 1次
print '----------'
print my_sum(2)		# 没有调用my_add, 返回2
print '----------'
print my_sum(None)	# 没有调用my_add, 返回None
print '----------'
print my_sum()   # TypeError: reduce() of empty sequence with no initial value 
print

print '-----------with init------------'
def my_com(x, y):
	print 'call: my_com(%s,%s)' % (x,y)
	return x if x>y else y

def my_max(*seq):
	print 'my_max(%s)' % `seq`
	return reduce(my_com, seq, -1)

print my_max(1,2)  # 调用my_com 2次 
print '----------'
print my_max(2)	   # 调用my_com 1次
print '----------'
print my_max(None) # 调用my_com 1次
print '----------'
print my_max()		# 未调用my_com, 直接返回None



#=======Output===========
'''
---------without init----------
my_sum((1, 2))
call:my_add(1,2)
3
----------
my_sum((2,))
2
----------
my_sum((None,))
None
----------
my_sum(())
TypeError:reduce() of empty sequence with no initial value

-----------with init------------
my_max((1, 2))
call: my_com(-1,1)
call: my_com(1,2)
2
----------
my_max((2,))
call: my_com(-1,2)
2
----------
my_max((None,))
call: my_com(-1,None)
-1
----------
my_max(())
-1
'''
