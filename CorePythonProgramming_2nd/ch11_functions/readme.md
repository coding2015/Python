chapter 11:
	Functions and Functional Programming


函数声明
	在Python中，函数声明即函数定义
	Python无类似C的函数声明(声明与定义分开)


lambda:
	匿名函数
	lambda args: expression
	等同于：
	def name(args):return expression
	
	eg:
		map(lambda x:x**2, range(10))


yield 语句：
	仅用在定义generator函数中


函数式编程：
	lambda
	BIFs: apply(), filter(), reduce(), map()
	偏函数：functools.partial(func,arg=val)
	前两项部分可被列表解析替代 


递归函数：
	可以递归的必要条件：
	有止
	有返回
	
