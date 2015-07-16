#coding:utf-8

'''
平分两个序列(长度一样)， 使其差尽可能小
合并，排序
递归：
	将最大元素添加到small, 将次大元素添加到big
	分别对small 与 big 求和， 若sum(small) > sum(big) 则交换
'''

def aver(big=[], small=[], total=None):
	print 'total:', total
	print 'big:  ',big
	print 'small:',small
	print 
	if not total:
		return (big, small)
	big.append(total[-2])	# 大的加次大元素
	small.append(total[-1])	# 小的加最大元素
	if sum(big) > sum(small):
		return aver(big, small, total[:-2])
	else:
		return aver(small, big, total[:-2])


test1 = [1,2,3,4,5,6,700,800]
test2 = [10001,10000,100,90,50,1]
test3 = [1,2,3,4,5,6,7,9,8,10]
test4 = [12312,12311,232,210,30,29,3,2,1,1]

test = [test1, test2, test3, test4]

for i in range(len(test)):
	print '\n==========test%d========' % (i+1) # ! i+1 需用括号 否则会被识别为fmstr+1
	test[i].sort()
	big, small = aver([], [], test[i])
	print 'result:', big, small
	print 'distance:', sum(big) - sum(small)


'''
$ python aver_lists.py 

==========test1========
total: [1, 2, 3, 4, 5, 6, 700, 800]
big:   []
small: []

total: [1, 2, 3, 4, 5, 6]
big:   [800]
small: [700]

total: [1, 2, 3, 4]
big:   [800, 5]
small: [700, 6]

total: [1, 2]
big:   [800, 5, 3]
small: [700, 6, 4]

total: []
big:   [800, 5, 3, 1]
small: [700, 6, 4, 2]

result: [800, 5, 3, 1] [700, 6, 4, 2]
distance: 97

==========test2========
total: [1, 50, 90, 100, 10000, 10001]
big:   []
small: []

total: [1, 50, 90, 100]
big:   [10001]
small: [10000]

total: [1, 50]
big:   [10000, 100]
small: [10001, 90]

total: []
big:   [10001, 90, 50]
small: [10000, 100, 1]

result: [10001, 90, 50] [10000, 100, 1]
distance: 40

==========test3========
total: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
big:   []
small: []

total: [1, 2, 3, 4, 5, 6, 7, 8]
big:   [10]
small: [9]

total: [1, 2, 3, 4, 5, 6]
big:   [9, 8]
small: [10, 7]

total: [1, 2, 3, 4]
big:   [10, 7, 6]
small: [9, 8, 5]

total: [1, 2]
big:   [9, 8, 5, 4]
small: [10, 7, 6, 3]

total: []
big:   [10, 7, 6, 3, 2]
small: [9, 8, 5, 4, 1]

result: [10, 7, 6, 3, 2] [9, 8, 5, 4, 1]
distance: 1

==========test4========
total: [1, 1, 2, 3, 29, 30, 210, 232, 12311, 12312]
big:   []
small: []

total: [1, 1, 2, 3, 29, 30, 210, 232]
big:   [12312]
small: [12311]

total: [1, 1, 2, 3, 29, 30]
big:   [12311, 232]
small: [12312, 210]

total: [1, 1, 2, 3]
big:   [12311, 232, 29]
small: [12312, 210, 30]

total: [1, 1]
big:   [12311, 232, 29, 2]
small: [12312, 210, 30, 3]

total: []
big:   [12311, 232, 29, 2, 1]
small: [12312, 210, 30, 3, 1]

result: [12311, 232, 29, 2, 1] [12312, 210, 30, 3, 1]
distance: 19

'''
