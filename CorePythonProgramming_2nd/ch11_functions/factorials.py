#!/usr/bin/python
#coding:utf-8
'''
Exercise 11-13:
	1.define three types of factorial function:
		a.normal:iter-loop 
		b.recursion
		c.reduce
	2.count the time-elaspe of these functions, using your timeit()

Factorial(N):
	N! = 1*2*3...*N
	1! = 0! = 1
KeyPoint:
	reduce()
	recursion
	timeit
'''

def facIter(n):
	ret = 1
	if n > 1:
		for x in range(1, n+1):
			ret *= x
	return ret


def facRecur(n):
	if n > 1:
		return n * facRecur(n-1)
	elif n in (0, 1):
		return 1
	else:
		return None


def facReduce(n):
	return reduce(lambda x,y:x*y, range(1,n+1))	


from timeit_ import timeit, multi_timeit

def main():
	funcs = (facIter, facRecur, facReduce)
	vals = (100, 200, 500, 700, 998) 
			#to recursion: when val >= 999, raise RuntimeError
	multi_timeit(funcs, False, *vals)

#	for eachFunc in funcs:
#		print '-'*30
#		for eachVal in vals:
#			ret = timeit(eachFunc, eachVal)
#			print ('%s(%s)' % (eachFunc.__name__, `eachVal`)).ljust(20), \
#					'time-elapsed(%.5f)s' %  ret[0]

	
if __name__ == '__main__':
	main()



'''
result:
每次运行结果都不一样，但观察几次结果，有如下规律：
iter方式效率最高，且其耗时随数字增长起伏不大
recursion方式开始调用时跟iter差不多，但耗时随数字增长起伏大
reduce方式在首次调用时耗时，随后的耗时曲线平缓，略高于iter方式
iter 优于 reduce 优于 recursion
------------------------------
facIter(100)         time-elapsed(0.00004)s
facIter(200)         time-elapsed(0.00005)s
facIter(500)         time-elapsed(0.00019)s
facIter(700)         time-elapsed(0.00032)s
facIter(998)         time-elapsed(0.00056)s
------------------------------
facRecur(100)        time-elapsed(0.00007)s
facRecur(200)        time-elapsed(0.00013)s
facRecur(500)        time-elapsed(0.00060)s
facRecur(700)        time-elapsed(0.00058)s
facRecur(998)        time-elapsed(0.00155)s
------------------------------
facReduce(100)       time-elapsed(0.00046)s
facReduce(200)       time-elapsed(0.00007)s
facReduce(500)       time-elapsed(0.00022)s
facReduce(700)       time-elapsed(0.00036)s
facReduce(998)       time-elapsed(0.00063)s

'''


