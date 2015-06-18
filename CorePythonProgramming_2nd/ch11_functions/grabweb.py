#!/usr/bin/python

'''
Example 11.4:
	This script downloads a Web page (defaults to local www server) and
	diaplays the first and non-blank lines of the HTML file.
	Flexibilly is added due to both default arguments of the download() function,  
	which will allow overriding with differet URLd or specification
	of a different processing function.
'''

from urllib import urlretrieve

def firstNonBlank(lines):
	for eachLine in lines:
		if not eachLine.strip():	#good idea to judge an empty line
			continue
		else:
			return eachLine

def firstLast(webpage):
	f = open(webpage)
	lines = f.readlines()
	f.close()
	print firstNonBlank(lines),
	lines.reverse() 	#good idea to reuse code
	print firstNonBlank(lines)

def download(url='http://www', process=firstLast):
	try:
		retval = urlretrieve(url)[0]
	except IOError:
		retval = None
	if retval:
		process(retval)

if __name__ == '__main__':
	#download() #output nothing
	download('https://github.com')
