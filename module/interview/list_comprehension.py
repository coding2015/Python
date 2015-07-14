#coding:utf-8

'''
列表解析
	用列表解析提取一个整数列表中索引值及其自身值都为偶数的元素

考察点: 列表解析， 序列切片操作
'''

# my solution 枚举法
>>> integers = [2,56,3,5,8,19,-10,-12]
>>> [e for i, e in enumerate(integers) if i%2==0 and e%2==0]
[2, 8, -10]


# standard solution 切片步长法
>>> [e for e in integers[::2] if e%2 == 0]	
[2, 8, -10]

