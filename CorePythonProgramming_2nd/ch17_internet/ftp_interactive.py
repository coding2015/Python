
'interactive FTP example'

>>> from ftplib import FTP
>>> ftp = FTP('ftp.debian.org')	  # connect to host, default port
>>> ftp.login()		# default, i.e.: user anonymous, passwd anonymous@
'230 Login successful.'
>>> ftp.dir()		# list directory contents
drwxr-xr-x    8 1176     1176         4096 Jun 30 03:24 debian
>>> ftp.cwd('debian')	# 切换路径
'250 Directory successfully changed.'
>>>
>>> ftp.retrlines('List')	# list directory contents, 同dir()
-rw-rw-r--    1 1176     1176         1493 Jun 06 10:19 README
-rw-rw-r--    1 1176     1176         1290 Jun 26  2010 README.CD-manufacture
-rw-rw-r--    1 1176     1176         3175 Jun 06 10:37 README.html
-rw-r--r--    1 1176     1176       187264 Jun 25 19:52 README.mirrors.html
-rw-r--r--    1 1176     1176        99350 Jun 25 19:52 README.mirrors.txt
drwxr-sr-x   22 1176     1176         4096 Jun 06 10:37 dists
drwxr-sr-x    4 1176     1176         4096 Jun 30 01:52 doc
drwxr-sr-x    3 1176     1176         4096 Jun 21 15:03 indices
-rw-r--r--    1 1176     1176     11505845 Jun 30 03:03 ls-lR.gz
drwxr-sr-x    5 1176     1176         4096 Dec 19  2000 pool
drwxr-sr-x    4 1176     1176         4096 Nov 17  2008 project
drwxr-xr-x    3 1176     1176         4096 Oct 10  2012 tools
'226 Directory send OK.'
>>> 
>>> ftp.retrbinary('RETR README', open('README','wb').write)  # 下载README文件
'226 Transfer complete.'
>>> ftp.quit()	# 退出登陆
'221 Goodbye.'


