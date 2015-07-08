#!/usr/bin/python
#coding:utf-8

class C(object):
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")


class C(object):
    def __init__(self):
        self._x = None
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    @x.setter
    def x(self, value):
		"setter"
		self._x = value
    @x.deleter
    def x(self):
        del self._x

'''
>>> c = C()
>>> c.x
>>> c.x = 10
>>> c.x
10
>>> del c.x
>>> c.x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in x
AttributeError: 'C' object has no attribute '_x'
>>> C.x.__doc__
"I'm the 'x' property."
'''

class Parrot(object):
    def __init__(self):
        self._voltage = 100000
    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

'''
>>> pt = Parrot()
>>> pt.voltage
100000
>>> pt.voltage = 12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
'''

# 将类外函数作为属性方法
from math import pi
def get_pi(dummy): # dummy as self 
	return pi

class PI(object):
	pi = property(get_pi, doc='Constant "PI"')

'''
>>> PI.pi
<property object at 0x7fd51ca91c58>
>>> 
>>> p = PI()
>>> p.pi
3.141592653589793
>>> PI.pi.__doc__
'Constant "PI"'
'''

# 将属性的方法inner化，使属性方法无法直接被实例调用，避免类名字空间混乱
class HideX(object):
	def __init__(self, data):
		self.__x = ~data 
	@property
	def x(self):
		def fget(self):
			print 'fget called'
			return ~self.__x	
		def fset(self, x):
			print 'fset called'
			assert isinstance(x, int), \
				'"x" must be an integer!'
			self.__x = ~x
		return locals()

'''
>>> h = pr.HideX(10)
>>> h.x
{'fset': <function fset at 0x7fd51ca94ed8>, 'self': <property.HideX object at 0x1c570d0>, 'fget': <function fget at 0x7fd51ca94e60>}
>>> h.x = 12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>> h.x['fget'](h)
fget called
-11
>>> h.x['fset'](h, -7)
fset called
>>> h.x['fget'](h)
fget called
-7
'''


# 非数据描述符优先级
class NonDes(object):
	def __init__(self, data):
		self.__data = data 
	def __get__(self, obj, type):
		return self.__data

class A(object):
	nd = NonDes('Nondata Des')	# 通过实例化非数据描述符类作为类属性

	def __init__(self, count=-1):
		self.__count = count

	@property			# 通过property装饰器定义非数据描述符属性
	def np(self):	
		return self.__count

'''
>>> a = pr.A()
>>> a.nd
'Nondata Des'
>>> a.np
-1
>>> a.nd = 12	# 实例属性 > 非数据类描述符属性
>>> a.np = 12	# 实例属性 < 非数据类描述符property属性
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
'''
