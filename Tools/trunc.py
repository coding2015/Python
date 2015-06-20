#!/usr/bin/python
#coding:utf-8
import sys
import os
'''
Tool:
	Truncating the names of a batch of files 

KeyPoint:
	str[:]
	sys.argv 命令行参数
	系统shell命令有些不奏效，需由os模块的相应方法实现
		os.path.exists(path/file) 	查看路径或文件是否存在
		os.chdir(path)	切换当前路径
		os.system('git mv name cutted')	重命名git文件	
		os.system('mv name cutted')		重命名非git文件

Experience:
	it's taken too much time to implement this tool(trunc-head)
	and almost lost consciousness in the end 
	which is very low effient and due to:
		1. too long of the main function codes
				which make it difficult to debug and easy to raise errors
				and lead to confused construction of the function
		2. too long of function names
		3. too much repeat of verifying a point
	ways to improve:
		1. make short name of function
		2. limit the function'a code-lines under 25
			if it exceeds, split the function to several functions
		3. be confident in your judgement and be as lazy as possible
		   and determin a set of test-data before execution

schedule:
	实现去头	done
	实现去尾	suspend
'''


def cutprefix(name, prefix):
	'return the name after cutting prefix'
	if prefix in name and len(prefix) < len(name):
		if name.find(prefix)==0:
			cut = name[len(prefix):]
			if cut[0].isalnum() or cut[0] == '_':
				return cut
	else:
		return None

		
def rename(old, new, isgit=False):
	'rename file from old to new'
	print 'rename(%s, %s, %s)' % (old, new, isgit)
	if isgit:
		cmd = 'git mv %s %s' % (old, new)
		os.system(cmd)
	else:
		cmd = 'mv %s %s' % (old, new)
		os.system(cmd)


def prepare():
	'''
	prepare before trunchead:
		examination arguments from cmdline
	'''
	if len(sys.argv) != 4:
		print 'invalid arguments\n\t should be like xxx.py -[l,g] path prefix'
		return
	if sys.argv[1] not in ('-g', '-l'):
		print 'invalid option\n\toption shoud be -g or -l\n-g: git\n-l:non-git'
		return
	if not os.path.exists(sys.argv[2]):
		print sys.argv[2], 'does not exist'
		return

	isgit = True if sys.argv[1]=='-g'else False
	fpath = sys.argv[2]
	prefix = sys.argv[3]

	return (fpath, prefix, isgit)


def trunchead():
	'''
	truncating the head of a batch files
	usage:
		 xxx.py -g path pre
		 xxx.py -l path pre
	'''
	
	args = prepare()
	if not args:
		return
	else:
		fpath, prefix, isgit = args

	os.chdir(fpath)
	files = os.listdir('.')
	
	for eachFile in files:
		cutted = cutprefix(eachFile, prefix)
		if cutted:
			rename(eachFile, cutted, isgit)

	files2 = os.listdir('.')
	print 'before rename:\nfiles(%d):\n' % len(files), files
	print 'after rename :\nfiles(%d):\n' % len(files2),files2
		
	#os.chdir(curpath) #不需此举，程序结束后会自动返回原来的目录

if __name__ == '__main__':
	trunchead()	


#============test functions==================
def test_cutprefix():
	"""
	this test proved that:
	cutprefix only cut the head of the name exactly equal to the given prefix
	and it's case sensitivity
	"""
	pre = 'str'
	vals = ('strtest','test_strteststr','Str.test','STR','str')
	for name in vals:
		cutted = cutprefix(name, pre)
		if cutted:
			print ('cut(%s):' % name).ljust(25) + cutted	
		else:
			print ('ncut(%s):' % name).ljust(25) + name	


def test_cutprefix_cmdline():
	if len(sys.argv) != 3: #!xxx.py is in sys.argv
		print  'invalid enter, "xxx.py name prefix"'
		return
	name = sys.argv[1]
	prefix = sys.argv[2]
	cutted = cutprefix(name, prefix)
	if cutted:
		print 'cutted:', cutted
	else:
		print 'nothing to cut', name


