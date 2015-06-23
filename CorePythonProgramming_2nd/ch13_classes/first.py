#!/usr/bin/python

class F:
	version = 1.0
	__doc__ = '''
	The very first class built in Python created by megan.
	method: info, members
	member:version, __doc__
	'''
	def __init__(self,name='NULL'):
		self.name = name
		print 'Created an instance for',name
	def info(self):
		print "This is an object called",self.name
		print "It's belongs to Class",self.__class__.__name__
	def members(self):
		print self.name,'has members:'
		print 'value =',self.version

name = raw_input('input an object name> ')
obj = F(name)
print 'info:'
obj.info()
print 'members:'
obj.members()
print 'F\'s __doc__:'
print F.__doc__
print 'list\'s __doc__:'
print list.__doc__
