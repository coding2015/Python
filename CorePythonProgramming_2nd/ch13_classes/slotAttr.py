#!/usr/bin/python
#coding:utf-8

'''
slotAttr.py

	性能需求：
		由于字典较消耗内存（同序列原因？）
		对于一个属性少但实例多的情况，将占用大量内存
	改进：
		用__slots__ 替代 __dict__

	__slots__ :
		限制了实例的属性
		实例不能增加自定义属性
			实例只能读不能改类的不可变静态变量(但可变静态变量可改)

KeyWord:
	improve performance 
	save memory usage
'''

class SlottedClass(object):
	__slots__ = ('foo', 'func')
	#__slots__ = ['foo', 'func'] # same as tuple type
	count = 1
	var = {'version': 1.0}
	data = [2,4,5,6]
	
	def func(self):
		print 'func() called'
		#self.value = 30   #Error
			#AttributeError: 'SlottedClass' object has no attribute 'value'

	def func2(self):
		print 'func2() called'


st = SlottedClass()
print st.__slots__
#print st.__dict__  #Error
#AttributeError: 'SlottedClass' object has no attribute '__dict__'

st.func()
st.func2()


print '\nvisit immutable static-member:'
print st.count
SlottedClass.count += 1
print st.count
#st.count += 1 	#Error
#AttributeError: 'SlottedClass' object attribute 'count' is read-only
st.foo = 12
#st.bar = 33	#Error
#AttributeError: 'SlottedClass' object has no attribute 'bar'


print '\nvisit and modify mutable static-members:'
print st.var
SlottedClass.var['version'] += 1
print st.var
st.var['version'] += 1
print st.var

print st.data
SlottedClass.data.append(15)
print st.data
st.data.append(89)
print st.data



#======Output==========
'''
('foo', 'func')
func() called
func2() called

visit immutable static-member:
1
2

visit and modify mutable static-members:
{'version': 1.0}
{'version': 2.0}
{'version': 3.0}
[2, 4, 5, 6]
[2, 4, 5, 6, 15]
[2, 4, 5, 6, 15, 89]

'''
