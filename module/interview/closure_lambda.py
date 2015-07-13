#coding:utf-8

'''
interview question

考察点: 闭包，自由变量
'''

print '\n%sOriginal%s\n' % ('*'*15, '*'*15)

def create_multipliers():
	return [lambda x: x*i for i in range(4)]

print [m(2) for m in create_multipliers()]  # [6, 6, 6, 6]


# 分析
# lambda ... 为闭包函数， i 为自由变量
# create_multipliers 等价于:

def create_multipliers():
	multipliers = []

	for i in range(4):
		def multiplier(x):
			return x * i
		multipliers.append(multiplier)

	return multipliers

# 调用闭包时访问的是动态的自由变量
# 故即使是先创建的闭包，最后访问i时的值都为i的最新值


########################################################
# 屏蔽自由变量

print '\n%sModify-1%s\n' % ('*'*15, '*'*15)

def multipliers():
	return [lambda x, i=i: x*i for i in range(4)]

print [m(2) for m in multipliers()]


########################################################
# patial(固定各个函数的默认参数)

print '\n%sModify-2%s\n' % ('*'*15, '*'*15)

from functools import partial
from operator import mul
def multipliers():
	return [partial(mul, i) for i in range(4)]

print [m(2) for m in multipliers()]

########################################################
# use generator(不用列表，调用时调用时动态产生函数）

print '\n%sModify-3%s\n' % ('*'*15, '*'*15)

def multipliers():
	for i in range(4): yield lambda x: x*i

print [m(2) for m in multipliers()]



'''
***************Original***************

[6, 6, 6, 6]

***************Modify-1***************

[0, 2, 4, 6]

***************Modify-2***************

[0, 2, 4, 6]

***************Modify-3***************

[0, 2, 4, 6]

'''
