#coding:utf-8

'Example 11.7'

output = '<int %r id=%#0x val=%d>'	# %#0x 0x-打印十六进制数，#-打印时带前缀0x
w = x = y = z = 1

def f1():
	x = y = z = 2

	def f2():
		y = z = 3

		def f3():
			z = 4
			print output % ('w', id(w), w)
			print output % ('x', id(x), x)
			print output % ('y', id(y), y)
			print output % ('z', id(z), z)

		clo = f3.func_closure	# 元组，f3的自由变量
		if clo:
			print 'f3.clo[%d]'% len(clo), clo
			print 'f3 closure vars:', [str(c) for c in clo]
		else:
			print 'no f3 closure vars'
		f3()


	clo = f2.func_closure
	if clo:
		print 'f2.clo[%d]'% len(clo), clo
		print 'f2 closure vars:', [str(c) for c in clo]
	else:
		print 'no f2 closure vars'
	print
	f2()


clo = f1.func_closure
if clo:
	print 'f1 closure vars:', [str(c) for c in clo]
else:
	print 'no f1 closure vars'
print
f1()



'''
no f1 closure vars

f2.clo[1] (<cell at 0x7fa01091d590: int object at 0x1cfec50>,)
f2 closure vars: ['<cell at 0x7fa01091d590: int object at 0x1cfec50>']

f3.clo[2] (<cell at 0x7fa01091d590: int object at 0x1cfec50>, <cell at 0x7fa01091d5c8: int object at 0x1cfec38>)
f3 closure vars: ['<cell at 0x7fa01091d590: int object at 0x1cfec50>', '<cell at 0x7fa01091d5c8: int object at 0x1cfec38>']
<int 'w' id=0x1cfec68 val=1>
<int 'x' id=0x1cfec50 val=2>
<int 'y' id=0x1cfec38 val=3>
<int 'z' id=0x1cfec20 val=4>
'''
