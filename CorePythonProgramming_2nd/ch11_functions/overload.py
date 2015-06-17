#!/usr/bin/python

'''
a test for overload functions
test result: 
	function defined later will overwrite(shield) 
		former-defined functions with the same name
		no mater they have different arguments 
conclude:
	python doesn't support overload as C/C++
'''

def fun():
	print 'origin'

#fun(19) #TypeError fun() takes no arguments 

def fun(x=1):
	print x

fun() #call fun(x)


def fun(x=2,y=3):
	print x,y


fun()  #call fun(x,y)
fun(9)	#call fun(x,y)
fun(x=10) #call fun(x,y)
