#!/usr/bin/python
#coding:utf-8
'''
Junior Customization:
	Example 13.2
'''

class RoundFloatManual(object):  
	def __init__(self, val):
		assert isinstance(val, float), "value must be float!"
		self.value = round(val, 2) 

	def test(self):
		return '%.2f' % self.value	

	__str__ = test	

	__repr__ = test

	#def __str__(self):	# used for print
	#	return '%.2f' % self.value

	#__repr__ = __str__	#used to show value when call instance itself	

if __name__ == '__main__':
	rfm = RoundFloatManual(12.3)
	print 'rfm:', rfm
	print 'rfm.value:', rfm.value
	print "repr:" , repr(rfm)
	print "``:" , `rfm`
