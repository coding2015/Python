#!/usr/bin/python

@contextmanager
def opened_w_error(filename, mode='r'):
	try:
		print 'open'
		f = open(filename, mode)
	except IOError, err:
		yield None, err
	else:
		try:
			yield f, None
		finally:
			print 'finally'
			f.close()


with opened_w_error("/home/megan/passwd", 'a') as (f, err):
	if err:
		print 'IOError:', err
	else:
		f.write('guido::0:0::/:/sbin/nologin\n')
