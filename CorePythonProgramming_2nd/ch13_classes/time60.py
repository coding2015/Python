#!/usr/bin/python

'''
Intermediate Customization:

Example 13.3

Exercise 13-20:
	1.allow empty args
	2.formate output with zero filling
	3.support varials enter formate
	*4.__radd__  
	5.correct __repr__, make its output a valid type (string)
	6.Add support for sexagesimal (base 60) operations
	
	Note:
	 '*'means undone
'''

class Time60(object):
	'Time60 - track hours and minutes'

	def __init__(self, hr=0, min=0, *args, **kwargs):
		'Time60 constructor - takes hours and minutes'
		if isinstance(hr, str):	 # process enter like: '12:30'
			time = hr.split(':')
			self.hr = int(time[0])
			self.min = int(time[1])
		elif isinstance(hr, dict): # process enter like: {'hr':10,'min':30}
			self.hr = hr['hr']
			self.min = hr['min']
		elif isinstance(hr, (tuple,list)):	# process enter like: (12, 30) 
			self.hr = hr[0]
			self.min = hr[1]
		else:
			self.hr = hr
			self.min = min

	
	def __str__(self):
		'Time60 - string representation'
		if self.min >= 60:
			(over, remain) = divmod(self.min, 60)
			self.hr += over
			self.min = remain
		return '%02d:%02d' % (self.hr, self.min)
	
	def __repr__(self):
		'Time60 - self value representation'
		#return repr(__str__(self))	#error
		return repr(self.__str__())

	def __add__(self, other):
		'Time60 - overloading the addition operator'
		return self.__class__(self.hr + other.hr,  self.min + other.min)  


	def __iadd__(self, other):
		'Time60 - overloading the in-place addtion'
		self.hr += other.hr
		self.min += other.min
		return self


if __name__ == '__main__':
	pass



