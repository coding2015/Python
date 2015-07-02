
'generator.throw()'

def counter(start_at=0):
        count = start_at
		time = 0
        while True:
            val = (yield count) 
			time += 1
            print '[%d]val:' % time , val   
            if val is not None:
                count = val
            else:
                count += 1

'''
>>> gen = counter()
>>> gen.next()
0
>>> gen.next()
[1]val: None
1
>>> gen.throw(BaseException,(12,'just throw exception:', 'by Jone'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in counter
BaseException: (12, 'just throw exception:', 'by Jone')
>>> 
>>> gen.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''
