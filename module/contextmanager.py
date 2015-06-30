#!/usr/bin/python
#coding: utf-8

'''
contextmanager:
	generator decoratot

apply for;
	with statement, etc

problem:
	how generator.throw work
'''

import sys

class GeneratorContextManager(object):
	'generator class'
	def __init__(self, gen):
		self.gen = gen
	
	def __enter__(self):
		try:
			return self.gen.next()
		except StopIteration:
			raise RuntimeError("generator didn't yield")

	def __exit__(self, type, value, traceback):
		if type is None:
			try:
				self.gen.next()
			except StopIteration:
				return
			else:
				raise RuntimeError("generator didn't stop")
		else:
			try:
				self.gen.throw(type, value, traceback)
				raise RuntimeError("generatot didn't stop after throw()")
			except StopIteration:
				return True
			except:
				if sys.exc_info()[1] is not value:
					raise

def contextmanager(func):
	'context manager'
	def helper(*args, **kwds):
		return GeneratorContextManager(func(*args, **kwds))
	return helper


#=========== example ==============
@contextmanager
def opened_w_error(filename, mode='r'):
	try:
		f = open(filename, mode)
	except IOError, e:
		yield None, e
	else:
		try:
			yield f, None
		finally:
			f.close()

'''
test data:

>>> reload(cm)
<module 'contextmanager' from 'contextmanager.py'>
>>> 
>>> with cm.opened_w_error('xxx') as (f, err):
...     if err:
...             print 'IOError:', err
...     else:
...             f.readlines()
... 
__enter__
return IOError
IOError: [Errno 2] No such file or directory: 'xxx'
__exit__: (None, None, None)
None: next
None: except return None
>>> 
>>> 
>>> with cm.opened_w_error('pass','a') as (f, err):
...     if err:
...             print 'IOError:', err
...     else:
...             f.write('github2:nologin\n')
... 
__enter__
return file obj
__exit__: (None, None, None)
None: next
close file
None: except return None
'''

#========example 2=============
'''
>>> @cm.contextmanager
... def opened(filename, mode='r'):
...     f = open(filename, mode)
...     if f:
...             yield f
...             print 'close file'
...             f.close()
... 
>>> with opened('pass') as f:
...     f.readlines()
... 
__enter__
['github:nologin\n', 'github2:nologin\n']
__exit__: (None, None, None)
None: next
close file
None: except return None
>>> 
'''
	
@contextmanager
def opened(filename, mode='r'):
     f = open(filename, mode)
     if f:
             yield f
             print 'close file'
             f.close()
     else:
             yield None
             print 'Nothing to close'
     print 'end'

'''
>>> with cm.opened('pass') as f:
...     f.write('info\n')
...     print 'with end'
... 
__enter__
__exit__: (<type 'exceptions.IOError'>, IOError('File not open for writing',), <traceback object at 0x7fd040c5cc20>)
notNone: throw
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IOError: File not open for writing
>>>
>>>
>>>
>>> with cm.opened('pass','a+') as f:
...     f.readlines()
...     f.write('info\n')
...     f.seek(0)
...     f.readlines()
... 
__enter__
[]
['info\n']
__exit__: (None, None, None)
None: next
close file
end
None: except return None


'''

