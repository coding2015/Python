#!/usr/bin/python
#coding:utf-8

'''
setuptools: an alternative of test-discover(python 2.7+), 
			which support older python-version
'''

from setuptools  import setup

setup(name='batTest', test_suite = 'firstEx')


'''
$ python setup.py test
running test
running egg_info
creating batTest.egg-info
writing batTest.egg-info/PKG-INFO
writing top-level names to batTest.egg-info/top_level.txt
writing dependency_links to batTest.egg-info/dependency_links.txt
writing manifest file 'batTest.egg-info/SOURCES.txt'
reading manifest file 'batTest.egg-info/SOURCES.txt'
writing manifest file 'batTest.egg-info/SOURCES.txt'
running build_ext
__name__: firstEx

testAdd (firstEx.MyCalTest) ... running set up
test done
running teardown
ok
testSub (firstEx.MyCalTest) ... running set up
test done
running teardown
ok
test_isupper (firstEx.MyCalTest) ... running set up
test done
running teardown
ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
'''
# 运行过程产生egg-info相关文件
'''
$ ls
batTest.egg-info  firstEx.egg-info firstEx.pyc ...
$ ls batTest.egg-info/
dependency_links.txt  PKG-INFO  SOURCES.txt  top_level.txt
$ ls firstEx.egg-info/
dependency_links.txt  PKG-INFO  SOURCES.txt  top_level.txt
'''
