#!/usr/bin/python
#coding:utf-8
"""
可变静态变量:
	通过实例可增删改可变静态变量的元素
	但不能通过实例删除可变静态变量本身
		否则报错AttributeError: class.xx is read-only

keyword:
	mutable static member
"""

class C(object):
	sta = {'version':1.0}


mc = C()
x  = C()
print "origin:"
print "mc.__dict__:", mc.__dict__
print "C.sta['version'] :" , C.sta['version']
print "mc.sta['version']:" , mc.sta['version']
print "x.sta['version'] :", x.sta['version'] 
print

mc.sta['version'] += 2	
print "mc.sta['version'] += 2"
print "mc.__dict__:", mc.__dict__
print "C.sta['version'] :" , C.sta['version']		
print "mc.sta['version']:" , mc.sta['version']	
print "x.sta['version'] :", x.sta['version'] 	
print

C.sta['version'] += 1
print "C.sta['version'] += 1"
print "mc.__dict__:", mc.__dict__
print "C.sta['version'] :" , C.sta['version']	
print "mc.sta['version']:" , mc.sta['version']	
print "x.sta['version'] :", x.sta['version']		
print

del mc.sta['version'] #KeyError: 'version'
print C.sta
#mc.sta = {}	 #相当于新建一个实例变量，遮蔽类静态变量
#del C.sta		#由类来删除类的静态变量
#print "mc.sta = {}"
#print "mc.__dict__:", mc.__dict__
#print "C.sta['version'] :" , C.sta['version']		
#print "mc.sta['version']:" , mc.sta['version']	
#print "x.sta['version'] :", x.sta['version']		
#print
#

#=====result=====
"""
origin:
mc.__dict__: {}
C.sta['version'] : 1.0
mc.sta['version']: 1.0
x.sta['version'] : 1.0

mc.sta['version'] += 2
mc.__dict__: {}
C.sta['version'] : 3.0
mc.sta['version']: 3.0
x.sta['version'] : 3.0

C.sta['version'] += 1
mc.__dict__: {}
C.sta['version'] : 4.0
mc.sta['version']: 4.0
x.sta['version'] : 4.0

{}
"""



