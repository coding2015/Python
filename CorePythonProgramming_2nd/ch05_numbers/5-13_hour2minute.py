def hour2minute():
	'conver h:m to m'
	time = raw_input('enter a time(h:m)> ')
	(h,m) = time.split(':')
	print '%s = %dm' % (time, int(h)*60 + int(m))


hour2minute()
