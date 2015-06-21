#!/usr/bin/python
from time import gmtime as gm
from os import path
import os 
ls = os.linesep
'''
Exercise 11-11:
	strip() all the lines of a file
	then let the user decide to overwite the file or create a new one	

KeyPoint:
	map()
	line comrehension
	new file's name: fname+time	
'''

def strip_data(fname):
	fobj =  open(fname)
	lines = fobj.readlines()
	fobj.close()
	
	#return map(strip(), lines)  #error, do not make effect at all
	return map(lambda x: x.strip(), lines)

	
def strip_lc(fname):
	'add omitting empty line'
	#return filter((lambda x: True if x else False), \
	#				 [line.strip() for line in open(fname)])
	return	[x for x in [line.strip() for line in open(fname)] if x]

	
def main():
	rfname = raw_input('enter a file name: ')
	if not path.exists(rfname):
		print rfname, 'does not exist.'
		return
	prompt = '(O)verwrite or (C)reate(default)? : '
	choice = raw_input(prompt)

	if choice and choice[0].lower() == 'o':
		wfname = rfname
	else:
		curtime = '%02d'*5 % \
			(gm().tm_mon, gm().tm_mday, gm().tm_hour+8, gm().tm_min, gm().tm_sec)
			# time-zone is American
		wfname = rfname + '_' + curtime
		
	newlines = strip_lc(rfname)
	fobj = open(wfname, 'w')
	#fobj.write(newlines) #write()'s argument required to be string
	fobj.writelines(['%s%s'% (line,ls) for line in newlines]) #add '/n'for each line
	fobj.close()

	print 'done, file:', wfname


if __name__ == '__main__':
	main()
