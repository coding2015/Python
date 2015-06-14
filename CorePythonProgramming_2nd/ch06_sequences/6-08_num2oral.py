#!/usr/bin/python
#coding:utf-8
'''
transform the numbers[1-1000] into oral language
'''

s0_19 ='''zero one two three four five six seven eight nine ten 
	eleven twelve thirteen fourteen fifteen sixteen 
	seventeen eighteen nineteen'''
s20_90 = '''twenty thirty forty fifty sixty seventy eighty ninety'''
N0_19 = s0_19.split()
N20_90 = s20_90.split()

while True:
	try:
		num = int(raw_input('enter an integer[0-1000]> '))
	except ValueError:
		print 'Invalid data, please enter an integer.'
	else:	
		if num < 0 or num > 1000:
			print 'The integer is out of range[0,1000], please try again.'  
		else:
			break

oral = []
if num <= 19:
	oral.append(N0_19[num])
else:
	q,r = divmod(num,100)
	if q > 0:
	   oral.append(N0_19[q]+'-hundred')
	if r > 0:
		if r <= 19:
			oral.append(N0_19[r])
		else:
			#q,r = divmod(num,10) #error:此时被除数应为上一次的余数
			q,r = divmod(r,10)
			oral.append(N20_90[q-2])
			if r != 0:
				oral.append(N0_19[r])

print '-'.join(oral)
