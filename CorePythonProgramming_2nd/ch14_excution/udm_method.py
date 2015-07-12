#!/usr/bin/python
#coding:utf-8

'''
比较类中的三种方法：
	类方法，实例方法，静态方法
'''

class A(object):
	def func(self): pass # self用来接收python自动传入的实例，无论绑定还是未绑定调用
	
	@classmethod
	def bar(cls):pass	# cls用来接收由python自动传入的类对象

	@staticmethod
	def foo(*args):pass


print 'A:'
print 'A.func:'.ljust(12), A.func
print 'A.bar:'.ljust(12),  A.bar
print 'A.foo:'.ljust(12), A.foo
print 'A type:'
print 'A.func:'.ljust(12), type(A.func)
print 'A.bar:'.ljust(12),  type(A.bar)
print 'A.foo:'.ljust(12), type(A.foo)

print '-'*30

a = A()
print 'a:'
print 'a.func:'.ljust(12), a.func
print 'a.bar:'.ljust(12),  a.bar
print 'a.foo:'.ljust(12), a.foo
print 'a type:'
print 'a.func:'.ljust(12), type(a.func)
print 'a.bar:'.ljust(12),  type(a.bar)
print 'a.foo:'.ljust(12), type(a.foo)



'''
A:
A.func:      <unbound method A.func>
A.bar:       <bound method type.bar of <class '__main__.A'>>
A.foo:       <function foo at 0x7fc581cf6aa0>
A type:
A.func:      <type 'instancemethod'>
A.bar:       <type 'instancemethod'>
A.foo:       <type 'function'>
------------------------------
a:
a.func:      <bound method A.func of <__main__.A object at 0x7fc581cf4b50>>
a.bar:       <bound method type.bar of <class '__main__.A'>>
a.foo:       <function foo at 0x7fc581cf6aa0>
a type:
a.func:      <type 'instancemethod'>
a.bar:       <type 'instancemethod'>
a.foo:       <type 'function'>
'''
	


