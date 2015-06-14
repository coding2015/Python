#!/usr/bin/python

def IsLeapYear(year):
	"""
	Make a judgement of weather the given year is a leap year or not
	Leap year:
		year that can be divided exactly by 4 but not by 100
		or year that can be divided exactly by 400
	"""
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		return True
	else:
		return False


def main():
	print IsLeapYear.__doc__
	year = int(raw_input('enter a year> '))
	print "%d is a leap year: %s" % (year,IsLeapYear(year))


#Entry
if __name__ == '__main__':
	main()
