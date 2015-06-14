#!/usr/bin/python
#coding:utf-8
'test for shallow-copy and deep-copy.'
'''
拷贝：只对容器类型有效
浅拷贝：只拷贝对象引用，若对象包含可变元素，则修改可变元素，所有副本都将改变
'''

import copy
person = ['name',['savings',100.00]]
'shallow copy'
#hubby = person[:] #slice copy
#wifey = list(person) #factory func copy
#wifey = copy.copy(person)
'deep copy'
#hubby = wifey = copy.deepcopy(person) #这样仍是浅拷贝，‘=’
hubby = copy.deepcopy(person)
wifey = copy.deepcopy(person)

print 'id in [person,hubby,wifey]:'
print [id(x) for x in person, hubby, wifey]
print

def printId():
	print hubby, wifey
	print [id(x) for x in hubby]
	print [id(x) for x in wifey]
	print hubby[1] is wifey[1]
	print

printId()

hubby[0] = 'Joe'
wifey[0] = 'Jane'
printId()

hubby[1][1] = 50.00
printId()

wifey[1][1] = 150.00
printId() 
