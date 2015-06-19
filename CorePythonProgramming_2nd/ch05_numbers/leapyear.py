#!/usr/bin/python
#coding:utf-8
'''
Exercise 5-4:
	judge a given year is a leapyear

leap year:
	闰年：
		1.能被4整除但不能被100整除
		2.或能被400整除
		两个条件相似(能被400整除的当然也能被100整除)，但是仔细思量有区别：
			能被4和100整除的比如200 不能被400整除
		故从能被4整除的数中剔除能被100整除的数，在另外增加能被400整除的数
'''

def isleapyear(year):
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
	print isleapyear.__doc__
	year = int(raw_input('enter a year> '))
	print "%d is a leap year: %s" % (year,isleapyear(year))


#Entry
if __name__ == '__main__':
	main()
