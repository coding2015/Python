#coding:utf-8

'''
Interview question:
	what will be the output of the code below?
	How to modify the definition of extendList to produce the presumably desired behavior?

KeyPoints:
	1.默认参数的id在定义函数时已确定，不会随着调用而改变(除非传参来覆盖)
	2.list对象在赋值时为浅拷贝
'''

print '\n%sOriginal%s\n' % ('*'*15, '*'*15)

def extendList(val, list=[]):  # 此时list已为定值
	print 'id(extendList.list):'.ljust(22), id(list)
	list.append(val)
	return list


list1 = extendList(10)	# 浅拷贝, 此时list1 与 extendList中的list参数为同一个对象
print 'id(list1):'.ljust(22), id(list1), '\n'
list2 = extendList(123, [])
print 'id(list2):'.ljust(22), id(list2), '\n'
list3 = extendList('a')
print 'id(list3):'.ljust(22), id(list3), '\n'


print 'list1 = %s' % list1
print 'list2 = %s' % list2
print 'list3 = %s' % list3


'''
id(extendList.list):   140416358418048
id(list1):             140416358418048 

id(extendList.list):   140416358082320
id(list2):             140416358082320 

id(extendList.list):   140416358418048
id(list3):             140416358418048 

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
'''

################################
print '\n\n%sModify-1%s\n' % ('*'*15, '*'*15)

def extendList(val, list):  
	print 'id(extendList.list):'.ljust(22), id(list)
	list.append(val)
	return list

list1 = extendList(10, [])	
print 'id(list1):'.ljust(22), id(list1), '\n'
list2 = extendList(123, [])
print 'id(list2):'.ljust(22), id(list2), '\n'
list3 = extendList('a',[])
print 'id(list3):'.ljust(22), id(list3), '\n'


print 'list1 = %s' % list1
print 'list2 = %s' % list2
print 'list3 = %s' % list3


################################
print '\n\n%sModify-2%s\n' % ('*'*15, '*'*15)

def extendList(val, list=None):  # 这样改最好，可以兼容旧调用
	if list is None: # !'[]'!=None, 所以不能写成 if not list
		list = []
	print 'id(extendList.list):'.ljust(22), id(list)
	list.append(val)
	return list

list1 = extendList(10, [])	
print 'id(list1):'.ljust(22), id(list1), '\n'
list2 = extendList(123, [])
print 'id(list2):'.ljust(22), id(list2), '\n'
list3 = extendList('a',[])
print 'id(list3):'.ljust(22), id(list3), '\n'


print 'list1 = %s' % list1
print 'list2 = %s' % list2
print 'list3 = %s' % list3


