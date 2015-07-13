#!/usr/bin/python
#coding:utf-8

'''
Example 14.2
	Function Attributes
	Calling sys.exit() causes the python interpreter to quit.
Any integer argument to exit() will be returnted to the caller as the exit status,
which has a default value of 0.

应用：
	有条件地执行代码
	为函数定义测试体属性，执行测试时先检测函数是否有测试体，有的话就执行否则跳过；
	可用于回归测试，且避免了测试代码混合到产品代码中

keypoint:
	自定义函数属性
'''

def foo():
	return True

def bar():
	'bar() does not do much'
	return True

foo.__doc__ = 'foo() does not do much'
foo.tester = '''
if foo():
	print 'PASSED'
else:
	print 'FAILED'
'''

print 'dir()', dir()
print 

for eachAttr in dir():
	obj = eval(eachAttr)	# 返回对象本身
	if isinstance(obj, type(foo)):	# 通过type(foo) 取得function类型
		if hasattr(obj, '__doc__'):
			print '\nFunction "%s" has a doc string:\n\t%s' % (eachAttr, obj.__doc__)
		if hasattr(obj, 'tester'):
			print 'Function "%s" has a tester... executing' % eachAttr
			exec obj.tester
		else:
			print 'Function "%s" has no tester... skiping' % eachAttr
	else:
		print '"%s" is not a function' % eachAttr
