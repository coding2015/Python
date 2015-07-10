#!/usr/bin/python
#coding:utf-8

'''
test-discover:
	通过命令'python -m unittest discover' 自动运行名字以'test'打头的模块的测试用例	
'''
import unittest

class MyCal(object):
	'class to test'
	def add(self, a, b):
		return a + b

	def sub(self, a, b):
		return a - b


class MyCalTest(unittest.TestCase):
	'override test-fixture'
	def setUp(self):
		print 'running set up'
		self.mycal = MyCal()

	def tearDown(self):
		print 'running teardown'
		self.mycal = None	# 此时MyCal()的引用计数变为0， 解释器自动回收资源
	
	'design test-cases'
	def testAdd(self):
		self.assertEqual(self.mycal.add(-1,7), 6)
		print 'test done'		

	def testSub(self):
		self.assertEqual(self.mycal.sub(10,2), 8)
		print 'test done'

	def test_isupper(self):
		self.assertTrue('BAR'.isupper())
		print 'test done'
	
	def isstring(self):		# 因为没有以'test'打头命名，所以自动测试时未被识别为用例
		print 'funcname without test'	# 除非采用注册到suite中的方式
		self.assertTrue(isinstance(12, str))
		print 'test done'

def main1():
	'自组织测试用例'
	suite = unittest.TestSuite()
	suite.addTest(MyCalTest('testAdd'))	# 添加测试用例
	suite.addTest(MyCalTest('testSub'))	
	suite.addTest(MyCalTest('isstring')) 
	
	runner = unittest.TextTestRunner()
	runner.run(suite)

def main2():
	'由unittest模块自动搜寻以“test”打头的测试用例并运行'
	unittest.main()	 # 自动运行所有test-cases

if __name__ == '__main__':
	main1()
else:
	print '__name__: %s\n' % __name__


'''
$ python -m unittest discover
__name__: testFirstEx

running set up
test done
running teardown
.running set up
test done
running teardown
.running set up
test done
running teardown
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
'''
