
'the return value of yield'

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
0		# 本次yield产出
>>> gen.next()
[1]val: None	# 上次yield返回
1		# 本次yield产出
>>> gen.next()
[2]val: None
2
>>> gen.send(12)
[3]val: 12
12
>>> gen.next()
[4]val: None
13
>>> gen.send()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: send() takes exactly one argument (0 given)
>>> 
>>> gen.next()
[5]val: None
14
>>> gen.close()
>>> gen.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> gen.send(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''
