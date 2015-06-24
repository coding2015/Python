#!/usr/bin/python
#coding:utf-8
'''
Privacy
	private members/methods
		以双下划线开头：__var，__method()
	只能在类内调用，在类外调用会报错:AttributeError
'''

class Test(object):
	__count = 19	# 私有成员
	time = 8
	
	@classmethod
	def visitPrivateMem(cls):  # 访问私有成员	
		print '__count:', cls.__count
	
	@classmethod	
	def __privateFun(cls):		# 私有方法
		'private method with double underscore'
		print 'private method called'

	@classmethod
	def callPrivateFun(cls):	# 调用私有方法
		cls.__privateFun()


#======test data========
# 私有成员
'''
>>> privacy.Test.time
8
>>> privacy.Test.__count
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Test' has no attribute '__count'
>>> 
>>> privacy.Test.visitPrivateMem()
__count: 19
'''

# 私有方法
'''
>>> privacy.Test.__privateFun()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Test' has no attribute '__privateFun'
>>> 
>>> privacy.Test.callPrivateFun()
private method called
'''

