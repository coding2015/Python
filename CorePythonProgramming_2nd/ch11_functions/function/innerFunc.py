
'inner function'

def func():
    def inner():
            print 'inner'
    inner()

'''
>>> func()
inner
>>> 
>>> inner()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'inner' is not defined
>>> 
>>> func.inner()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'inner'
>>> 
'''
