
'closure'

def make_printer1(msg):
	def printer():		# printer is a closure
		print '1.',msg
	print 'clo1:',printer.func_closure
	return printer


def make_printer2(msg):
	def printer(msg=msg): # printer is not a closure
		print '2:',msg
	print 'clo2:', printer.func_closure
	return printer

make_printer1('foo')
make_printer2('foo')

'''
clo1: (<cell at 0x7f3da61f1398: str object at 0x7f3da61f4da0>,)
clo2: None
'''
