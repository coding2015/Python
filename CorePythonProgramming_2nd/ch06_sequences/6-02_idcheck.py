#!usr/bin/python
#coding:utf-8
'''
Tests for identifier validity.

Premise:identifier shouldn't be a keyword.
If the length of the charaters is 1:
	then:the identifier must be letters
else the length of the charaters > 1:
	then:First symbol must be alphabetic (letters+_)
		 and remaining symbols must be alphanumeric.
'''

import string
import keyword

letters = string.letters
alphas = letters + '_'
nums = string.digits
alphnums = alphas + nums
keywords = keyword.kwlist
okay = 'Okay as an identifier.'

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long'
myInput = raw_input('Intentifier to test? ')


#先判断是否是关键字再判断合法性，效率会高些
#否则最后合法了到头来却发现竟是关键字，怎么都不合算
if myInput in keywords:
	print '''invalid:
		identifier shouldn't be a keyword.'''

elif len(myInput) == 1:
	if myInput not in letters:
		print '''invalid:
			identifier with 1 character in length should be a letter.'''
	else:
		print okay
else:
	if myInput[0] not in alphas:
		print '''invalid: first symbol must be 
			alphabetic'''
	else:
		for otherChar in myInput[1:]:
			
			if otherChar not in alphnums:
				print '''invalid: remaining
					symbols must be alphanumeric'''
				break
		else:
			print "Okay as an identifier"	
	
