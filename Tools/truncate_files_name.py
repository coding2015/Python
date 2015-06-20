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
		os.chdir(path) 切换当前路径
		os.system('git mv name cutted')	重命名git文件	
		os.system('mv name cutted')		重命名非git文件

schedule:
	实现去头			done
	命令行传参			done
	修改文件名  
	批量修改文件名
	命令选项 -p,-x,..
	实现去尾
'''


def truncate_head(name, prefix):
	if prefix in name and len(prefix) < len(name):
		if name.find(prefix)==0:
			return name[len(prefix):]
	else:
		return None
		
def rename_file(old, new, isgit=False):
	print 'rename_file(%s, %s, %s)' % (old, new, isgit)
	if isgit:
		cmd = 'git mv %s %s' % (old, new)
		os.system(cmd)
	else:
		cmd = 'mv %s %s' % (old, new)
		os.system(cmd)

def rename_files_cutprefix():
	'''
	usage:
		 xxx.py -g path pre
		 xxx.py -l path pre
	'''
	# arguments examination
	if len(sys.argv) != 4:
		print 'invalid arguments\n\t should be like xxx.py -[l,g] path prefix'
		return
	if sys.argv[1] not in ('-g', '-l'):
		print 'invalid option\n\toption shoud be -g or -l\n-g: git\n-l:non-git'
		return
	if not os.path.exists(sys.argv[2]):
		print sys.argv[2], 'does not exist'
		return

	print 'arguments:ok'	
	isgit = True if sys.argv[1]=='-g'else False
	fpath = sys.argv[2]
	prefix = sys.argv[3]


	# prefix truncation
	curpath	= os.getcwd()
	print 'curdir:', curpath
	os.chdir(fpath)
	print 'curdir:', os.getcwd()
	
	files = os.listdir('.') #注意，已经切换到操作目录
							  #所以除非能保证fpath是绝对路径，否则此处最好‘.’
	print
	print 'before rename:\nfiles(%d):\n' % len(files), files
	
	cuttimes = 0
	for eachFile in files:
		cutted = truncate_head(eachFile, prefix)
		if cutted:
			rename_file(eachFile, cutted, isgit)
			cuttimes += 1

	files = os.listdir('.')
	print
	print 'after rename(%d):\nfiles(%d)\n'% (cuttimes,len(files)),files
		
	#os.chdir(curpath) #不需此举，程序结束后会自动返回原来的目录
	#print os.getcwd()

if __name__ == '__main__':
	rename_files_cutprefix()	


#============test functions==================
def test_cutprefix():
	"""
	this test proved that:
	truncate_head only cut the head of the name exactly equal to the given prefix
	and it's case sensitivity
	"""
	pre = 'str'
	vals = ('strtest','test_strteststr','Str.test','STR','str')
	for name in vals:
		cutted = truncate_head(name, pre)
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
	cutted = truncate_head(name, prefix)
	if cutted:
		print 'cutted:', cutted
	else:
		print 'nothing to cut', name


