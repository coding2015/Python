#!/usr/bin/python
#coding:utf-8

'''
break in try section
to see if except or else or finally part excuted

conclusion:
	在try中break后except与else都不会执行
	但finally会执行
'''

def breakEx():
	while True:
		try:
			break
		except:
			print 'except'
		else:
			print 'else'
		finally:
			print 'finally'


'''
>>> tb.breakEx()
finally
'''
