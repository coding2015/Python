'异常上发'

>>> def readfile(filename):
...     [line for line in open(filename)]
... 
>>> def test():
...     readfile('xxx')
... 
>>> try:
...     test()
... except BaseException, e:
...     print repr(e)
... 
IOError(2, 'No such file or directory')


