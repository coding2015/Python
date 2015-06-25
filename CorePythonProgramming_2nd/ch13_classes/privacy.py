#!/usr/bin/python
#coding:utf-8
'''
Privacy
	private members/methods
		以双下划线开头：__var，__method()
	只能在类内调用，在类外调用会报错:AttributeError
	原因：
		由双下划线打头的属性在类或实例的命名空间名字被改变(可查看其字典)
		__xxx 在字典中显示的名字为 _classname__xxx
		通过后者仍可以访问该私有属性
'''

class Test(object):
	__count = 19	# 私有成员
	time = 8

	def __init__(self):
		self.__data = 'self.private.data' 
		self.value = 'self.value'
	
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
>>> pt = privacy.Test('data')
>>> 
>>> pt.__data
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Test' object has no attribute '__data'
>>> 
>>> pt.value
'data'
>>> pt.__dict__
{'_Test__data': 'data', 'value': 'data'}
>>>
>>> pt._Test__data	 #私有变量的真在名字
'self.private.data'
'''


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
>>>
>>> privacy.Test.__dict__
dict_proxy({'_Test__privateFun': <classmethod object at 0x7fa0ac54c280>, '__module__': 'privacy', '__init__': <function __init__ at 0x7fa0ac5505f0>, 'callPrivateFun': <classmethod object at 0x7fa0ac54c2f0>, 'time': 8, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '_Test__count': 19, 'visitPrivateMem': <classmethod object at 0x7fa0ac54c248>, '__doc__': None})
>>>
>>> privacy.Test.__dict__.has_key('_Test__data')
False
>>> privacy.Test.__dict__.has_key('_Test__count') #私有静态变量的真在名字
True
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
>>>
>>> privacy.Test._Test__privateFun()  # 私有方法的真正名字
private method called
'''

