
'usage of yield statement'

def foo(x):
	print 'foo:',x

def func():
    x = yield 42  # 第1次next()返回
    y = yield	  # 第2次next()返回	
    print x, y	  # None None
	foo((yield 42)) # 第3次next()先返回yield 42, 下一个next()再调用foo()

    #x = 12 + yield # SyntaxError，在表达式中的yield需用括号包含
	#x = 12 + (yield 42)	# error
		# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
	#y = 12 + (yield)

'''
>>> gen = func()
>>> gen.next() 	#1
42
>>> gen.next()	#2
>>> gen.next()	#3
None None
42
>>> gen.next()	#StopIteration
foo: None
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''


def func():
    x = yield 42
    y = yield 0
    print 'x,y', x,y
    yield 'end'

''' 
>>> gen = func()
>>> gen.next()
42
>>> gen.send(77)
0
>>> gen.send(3)
x,y 77 3
'end'
'''


