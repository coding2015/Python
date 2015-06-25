#!/usr/bin/python
#coding:utf-8
'''
Study;
	学习已被覆盖的基类方法，如何被子类对象调用

call parent's method from child
	1.	P.method(c_instance)
	2.	in C.method:
			super(C, self).method()	#比1先进之处，不需交代基类名
									#即使修改了继承关系, 这里也不需改动
keyword:
	BIF
	inheritance

KeyPoint:
	super(type, instance).method(args)	
		super()找不到调用父类的静态方法
	new-style-classes.__mro__   方法搜索顺序	

Question:
	若是多重继承，super找谁？
Answer:
	不同的继承结构，查找顺序不同
	可通过类的__mro__属性查看其查找顺序
	1.| |
 	  | |
	  \/
		按继承顺序从左往右查找基类的方法
		先找第一个基类，若没有继续查找该基类的基类， ...
		问候遍第一个基类的祖宗十八代仍没有的话，问候第二个基类， ...
	2.|\/|
	  |/\|
	   \/
		按继承层次查找
		先从第一层按从左到右查找(子类的直接继承层)
		找不到再找第二层
'''

class Base(object):
	def fun1(self):
		print '\tP.fun1(%s)'% self.__class__.__name__

	def fun3(self):	
		print '\tBase.fun3(%s)' % self.__class__.__name__

class Base2(object):
	pass

	
class P(Base):
	def fun1(self):
		print '\tP.fun1(%s)'% self.__class__.__name__

	def fun2(self, data):
		print '\tP.fun2(%s, %s)'% \
				(self.__class__.__name__, `data`)

class P2(Base2):
	def fun1(self):
		print '\tP2.fun1(%s)'% self.__class__.__name__
	
	def fun2(self, data):
		print '\tP2.fun2(%s, %s)'% \
				(self.__class__.__name__, `data`)

	def fun3(self):
		print '\tP2.fun3(%s)' % self.__class__.__name__

	@staticmethod
	def staticFun():
		print 'P2.staticFun() called'

	@classmethod
	def classFun(cls):
		print 'P2.classFun(%s) called' % cls

class C(P, P2):
	def fun1(self):
		print 'C.fun1(%s)'% self.__class__.__name__
		super(C, self).fun1()


	def test(self, data):
		print 'C.test(%s, %s)' % (self.__class__.__name__, `data`)
		super(C, self).fun1()
		super(C, self).fun2(data)
		super(C, self).fun3()
		
		#super(C).staticFun() #Error
			#AttributeError: 'super' object has no attribute 'staticFun' 
	
		super(C, self).classFun()

print 'unbound call:'
ct = C()
ct.fun1()
P.fun1(ct)
print

print 'super():'
ct.fun1()
ct.test(59)
print

print 'C.__mro__'
print C.__mro__

#======Output========
#类结构
#	Base	Base2	  |	|
#	P		P2		  |	|
#		 C			  \/
'''
unbound call:
C.fun1(C)
	P.fun1(C)
	P.fun1(C)

super():
C.fun1(C)
	P.fun1(C)
C.test(C, 59)
	P.fun1(C)
	P.fun2(C, 59)
	Base.fun3(C)

C.__mro__
(<class '__main__.C'>, <class '__main__.P'>, <class '__main__.Base'>, <class '__main__.P2'>, <class '__main__.Base2'>, <type 'object'>)
'''

#类结构
#	Base Base2	|\/|
#	  P	P2		|/\|
#	   C		 \/
'''
unbound call:
C.fun1(C)
	P.fun1(C)
	P.fun1(C)

super():
C.fun1(C)
	P.fun1(C)
C.test(C, 59)
	P.fun1(C)
	P.fun2(C, 59)
	P2.fun3(C)

C.__mro__
(<class '__main__.C'>, <class '__main__.P'>, <class '__main__.P2'>, <class '__main__.Base'>, <class '__main__.Base2'>, <type 'object'>)
'''

