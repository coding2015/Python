#coding:utf-8
'''
with statement:
	等价于try-except-finally, 并回收资源
	仅作用于支持上下管理协议的对象，eg: file, thread.LockType, ...

contextmanager(上下文管理器),至少包含以下两种属性:
	__enter__(self, agrs) -> var
	__exit__(self, type, value, trace) -> bool
							 # 资源回收
							 # 处理异常，若不处理则返回False让with之后代码处理

statement:
	with mgr as var: blockd
等价于:
	exc = True
	try:
		try: 
			var = mgr.__enter__()
			block
		except:
			exc = False
			if not mgr.__exit__(*sys.exc_info()) 
				raise
	finally:
		if exc:
			mgr.__exit__(None, None, None)
'''

class ContextManager(object):
	def __init__(self):
		print self.__class__.__name__, '__init__'
		pass

	def __enter__(self):
		'dispatch source'
		print self.__class__.__name__, '__enter__'
		pass
	
	def __exit__(self, type, value, trace):
		'recycle source'
		print self.__class__.__name__, '__exit__:',(type, value, trace) 
		if type is None:
			return 
		else:
			print 'err:', value 
			return True


'''
>>> mgr = cm.ContextManager()
ContextManager __init__
>>> 
>>> with mgr as var:
...     pass
... 
ContextManager __enter__
ContextManager __exit__: (None, None, None)


>>> with mgr as var:
...     float('er')
... 
ContextManager __enter__
ContextManager __exit__: (<type 'exceptions.ValueError'>, ValueError('could not convert string to float: er',), <traceback object at 0x7fd040c5b560>)
err: could not convert string to float: er
>>> 


'''	
