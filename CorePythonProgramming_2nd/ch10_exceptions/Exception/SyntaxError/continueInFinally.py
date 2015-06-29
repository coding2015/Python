>>> while True:
...     try:
...         try:
...             1/0
...         finally:
...             continue
...     except BaseException, e:
...         print 'outside:\t', e
... 
  File "<stdin>", line 8
SyntaxError: 'continue' not supported inside 'finally' clause

