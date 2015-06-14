#!/usr/bin/python

'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter filename: ')
print

# attempt to open file for reading
#try:
#	fobj = open(fname,'r')
#except IOError,e:
#	print "*** file open error:",e
#else:
#	# display contents to the screen
#	for eachLine in fobj:
#		print eachLine,
#	fobj.close()


import os
if not os.path.exists(fname):
	print fname,"doesn't exist"
else:
	#display the file's contents to the screen
	fobj = open(fname,'r')
	for line in fobj:
		#strip() 去掉每行末尾的所有空白符号
		print line.strip()
	fobj.close() 
