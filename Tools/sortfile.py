#!/usr/bin/python
import os.path

fname = raw_input('enter a file: ') 
if not os.path.exists(fname):
	print "file does not exist" 
	#return # error, return used only in function
	exit(-1)

fobj = open(fname)
lines = fobj.readlines() 
fobj.close() 

#enter two line numbers
beg	= int(raw_input('beg line> '))
end	= int(raw_input('end line> '))
sortlines = lines[beg-1 : end-1]
sortlines.sort()
#sortlines = (lines[beg-1, end-2]).sort() #None
newlines = lines[:beg] + sortlines + lines[end:]

fobj = open(fname, 'w')
fobj.writelines(newlines)
fobj.close()

print 'done'

