#!/usr/bin/python
#coding:utf-8

'''
Example 14.1
	Dynamically Generating and Executing Python Code

动态创建代码并执行
'''


dashes = '\n' + '-' * 50	# 破折线
exec_dict = {
'f': """
for %s  in %s:		# for loop
	print %s
""",

's': """			# sequences while loop				
%s = 0		
%s = %s
while %s < len(%s):
	print %s[%s]
	%s = %s +1
""",

'n': """			# counting while loop
%s = %d
while %s < %d:
	print %s
	%s = %s + %d
"""
}

def main():
	
	ltype = raw_input('Loop type? (For/While)')
	dtype = raw_input('Data type? (Number/seq)')
	
	if dtype == 'n':
		start = input('Starting value? ')
		stop = input('Ending Value (non-inclusivw)? ')
		step = input('Stepping value? ')
		seq = str(range(start, stop, step))
	else:
		seq = raw_input('Enter sequence: ')
	
	var = raw_input('Iterative variable name? ')
	
	if ltype == 'f':
		exec_str = exec_dict['f'] % (var, seq, var)
	elif ltype == 'w':
		if dtype == 's':
			svar = raw_input('Enter sequence name? ')
			exec_str = exec_dict['s'] % \
				(var, svar, seq, var, svar, svar, var, var, var) 
		elif dtype == 'n':
			exec_str = exec_dict['n'] % \
				(var, start, var, stop, var, var, var, step)

	print dashes
	print 'Your custom-generated code:' + dashes
	print exec_str + dashes
	print 'Test execution of the code:' + dashes
	exec exec_str
	print dashes

if __name__ == '__main__':
	main()


'''
$ python loopmake.py 
Loop type? (For/While)f
Data type? (Number/seq)n
Starting value? 1
Ending Value (non-inclusivw)? 10
Stepping value? 1
Iterative variable name? count

--------------------------------------------------
Your custom-generated code:
--------------------------------------------------

for count  in [1, 2, 3, 4, 5, 6, 7, 8, 9]:		# for loop 
	print count

--------------------------------------------------
Test execution of the code:
--------------------------------------------------
1
2
3
4
5
6
7
8
9

--------------------------------------------------
'''
