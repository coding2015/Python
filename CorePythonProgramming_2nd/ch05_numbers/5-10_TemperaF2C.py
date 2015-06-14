from __future__ import division

def F2C(tf):
	"Temperature coversion from F to C"
	tc = (tf  - 32) * (5/9)
	return tc

def main():
	print F2C.__doc__
	tf = float(raw_input('enter a temperature value in F> '))
	print "%.1fF = %.1fC" % (tf,F2C(tf))


if __name__ == '__main__':
	main()
