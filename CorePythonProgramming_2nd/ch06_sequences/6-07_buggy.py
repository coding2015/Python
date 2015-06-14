#coding:utf-8

# 输入一个数字
num_str = raw_input('Enter a number: ')

# 将字符串转换为数字
num_num = int(num_str)

# 创建一个个数为num，元素值从1到num+1的数字列表
fac_list = range(1, num_num+1)
print "BEFORE:", `fac_list`

# 
i = 0
#
while i < len(fac_list):
	#print i
	# 如果num可以被列表元素整除，就删除列表元素
	if num_num % fac_list[i] == 0:	
		print 'del (%d,%d)' % (i,fac_list[i])
		del fac_list[i]
	else:
		i = i + 1

#
#def PrintL(l):
#	for e in enumerate(l):
#		print e
#
#for i,e in enumerate(fac_list):
#	print i
#	if num_num % e == 0:
#		PrintL(fac_list)
#		print 'del:(%d,%d)'% (i,e)
#		del fac_list[i]
#		i -= 1 #cannot control i, i is determined by for
#		PrintL(fac_list)
#		print 
#
print "AFTER:", `fac_list`
