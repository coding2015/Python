#!usr/bin/python

'''
Example 17.1
	FTP Download Example
	This program is used to download the latest version of a file from a web site.
'''

import ftplib
import os
import socket

HOST = 'ftp.debian.org'
DIRN = 'debian/tools'
FILE = 'loadlin.exe'

def main():
	try:
		f = ftplib.FTP(HOST)	# connect ftp
	except (socket.error, socket.gaierror), e:	# what? 
		print 'ERROR: cannot reach "%s"' % HOST
		print 'e:\t', e
		return 
	print '*** Connected to host "%s"' % HOST

	try:
		f.login()		# login
	except ftplib.error_perm, e:	# what?
		print 'ERROR: cannot login anonymously'
		print 'e:\t', e
		f.quit()
		return
	print '*** Logged in as "anonymous"'
	
	try:
		f.cwd(DIRN)		# change to target directory
	except ftplib.error_perm, e:
		print 'ERROR: cannot CD to "%s"' % DIRN
		print 'e:\t', e
		f.quit()
		return
	print '*** Changed to "%s" folder' % DIRN
	
	try:
		loc = open(FILE, 'wb')
		f.retrbinary('RETR %s' % FILE, loc.write)
	except IOError, e:	# there are possible error may raise during open and write
		print 'IOError:\t', e
		loc.close()
	except ftplib.error_perm, e:
		print 'ERROR: cannot read file "%s"' % FILE
		print 'e:\t', e
		os.unlink(FILE)	# del file
	else:
		loc.close()		# close file
		print '*** Downloaded "%s" to %s' % (FILE, `os.getcwd()`)	
	f.quit()
	return

if	__name__ == '__main__':
	main()


#=======Output===========
'''
$ python getLatestFTP.py 
ERROR: cannot reach "ftp:debian.org"
e:	[Errno -2] Name or service not known


$ python getLatestFTP.py 
*** Connected to host "ftp.debian.org"
*** Logged in as "anonymous"
*** Changed to "debian/tools" folder
*** Downloaded "loadlin.exe" to '/home/megan/Githubs/Python/CorePythonProgramming_2nd/ch17_internet'

'''


