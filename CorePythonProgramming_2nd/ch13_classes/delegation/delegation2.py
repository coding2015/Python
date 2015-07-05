#!/usr/bin/python
#coding:utf-8

'''
__getattribute__:
	不同于__getattr__(找不到当前类属性才去访问默认属性)
	访问任一属性，都会调用__getattribute__ 

keyword:
	delegation
	customization

keypoint:
	成员变量也是属性，可以被getattr识别
	交互模式下直接输出变量名时，
		会调用__repr__
		如果__repr__返回是成员的属性的话，会继续调用__getattribute__
			此时类似管道，__repr输出的属性作为__getattrbute__的输入
			but why: 为何返回的是成员属性的字符串形式，也能被识别为属性
'''

class Wrap2(object):
	def __init__(self, obj):
		self.datas = obj
		self.version = 1.0

	def __repr__(self):
		print '__repr__ called'
		#return `self.datas`
		#return `self.version`		
		#return ''
		#return 'test'
		#self.temp = 'temp'
		#return `self.temp`
		#x = 12
		#return `x`
		#return str(self.datas)
		s = str(self.datas)
		return s

	def get(self):
		return self.datas


	def __getattr__(self, attr):
		print '__getattr__(%s, %s)' % (self.__class__.__name__, attr)
		return getattr(self.datas, attr)


	def	__getattribute__(self, attr):
		#print '__getattrbute__(%s, %s)' % (self.__class__.__name__, attr)
		#RuntimeError: again，似乎在此调用了self就会导致无限递归
		print '__getattibute__, attr:', attr

		#return getattr(self.datas, attr) #RuntimeError:无限递归, Why?
		return super(Wrap2, self).__getattribute__(attr)


#======Test Data========
'''
>>> wr
__repr__ called
__getattibute__, attr: datas   #注意：方法和变量都是属性！！
[1, 2, 3, 4]
>>> 
>>> wr.append(90)
__getattibute__, attr: append
__getattibute__, attr: __class__
__getattr__(Wrap2, append)
__getattibute__, attr: datas
>>> 
'''
#不同__repr__返回时的输出
'''
__repr__返回：
		#return `self.datas`
		#return `self.version`		
		#return ''
		#return 'test'
		#self.temp = 'temp'
		#return `self.temp`
		#x = 12
		#return `x`
		#return str(self.datas)
		s = str(self.datas)
		return s

对应输出：
>>> wr
__repr__ called
__getattibute__, attr: datas	#成员属性
[1, 2, 3, 4]
>>>
>>> wr
__repr__ called
__getattibute__, attr: version	 #成员属性
1.0
>>> wr
__repr__ called
						#非成员属性
>>> wr
__repr__ called
test					#非成员属性
>>> wr
__repr__ called
__getattibute__, attr: temp		#成员属性
'temp'
>>> wr
__repr__ called			#非成员属性
12
>>>
>>>wr
__repr__ called
__getattibute__, attr: datas	#return str(self.datas)
[1, 2, 3, 4]
>>>wr
__repr__ called
__getattibute__, attr: datas	#return s
[1, 2, 3, 4]

'''
