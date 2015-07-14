#coding:utf-8

'''
考察点: 传统除法， 地板除

地板除： 无论何种数值类型， 结果都舍去小数，取小于商的最大整数(但类型不变)
传统除法: 对整数采取地板除，对浮点数采取真正除法
'''

print '\n%sOriginal%s\n' % ('-'*15, '-'*15)

def div1(x, y):		# 传统除法
	print '%s/%s = %s' % (x, y, x/y)

def div2(x, y):		# 地板除
	print '%s/%s = %s' % (x, y, x//y)

div1(5, 2)		# 2
div1(5., 2)		# 2.5
div2(5, 2)		# 2
div2(5., 2)		# 2.0, 舍去小数部分，但仍为浮点数


'''
延伸：

真正除法/:
		from __future__ import division
		未来版本操作符 / 对任何类型的操作数都采取真正除法		


值保留 int() vs // vs round()
		int(n): 取整，舍去小数部分
				n>0, int(n) <= n
				n<0, int(n) >= n
		floor(n): 取小于商的最大整数 (不存在floor()函数，此处为方便比较故记此)
				无论n为何值, floor(n) <= n
		round(n): 四舍五入	 
				n>0时，四舍<=n,五入>n
                		n<0时，四舍>=n.五入<n	
'''
