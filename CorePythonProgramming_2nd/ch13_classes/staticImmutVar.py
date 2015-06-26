#!/usr/bin/python
#coding:utf-8
'''
不可变静态变量
	类的不可变静态变量只能通过类更新，
	由实例来更新或设定静态变量，则对该实例而言，新属性被创建而类的静态变量被遮蔽

keyword:
	immutable static member
'''

class C(object):
	version = 1.0


mc = C()
x  = C()
print 'origin:'
print 'mc.__dict__:', mc.__dict__
print 'C.version :' , C.version
print 'mc.version:' , mc.version
print 'x.version :', x.version 
print

mc.version += 2		#实际上: mc.version = mc.version + 1, 实例新建了一个属性
print 'mc.version += 2'
print 'mc.__dict__:', mc.__dict__
print 'C.version :' , C.version		# 1.0
print 'mc.version:' , mc.version	# 3.0
print 'x.version :', x.version 		# 1.0
print

C.version += 1
print 'C.version += 1'
print 'mc.__dict__:', mc.__dict__
print 'C.version :' , C.version		# 2.0
print 'mc.version:' , mc.version	# 3.0
print 'x.version :', x.version		# 2.0
print

del mc.version
print 'del mc.version '
print 'mc.__dict__:', mc.__dict__
print 'C.version :' , C.version		# 2.0
print 'mc.version:' , mc.version	# 2.0
print 'x.version :', x.version		# 2.0
print


#=====result=====
'''
rigin:
mc.__dict__: {}
C.version : 1.0
mc.version: 1.0
x.version : 1.0

mc.version += 2
mc.__dict__: {'version': 3.0}
C.version : 1.0
mc.version: 3.0
x.version : 1.0

C.version += 1
mc.__dict__: {'version': 3.0}
C.version : 2.0
mc.version: 3.0
x.version : 2.0

del mc.version 
mc.__dict__: {}
C.version : 2.0
mc.version: 2.0
x.version : 2.0

'''



