#!/usr/bin/python
#coding:utf-8

def Dollar2Cents(dollar):
	"""
	Convert the given amount of dollar to as little as possible.
	Kinds of Cent:	
		25-cent value, 10-cent value, 5-cent value, 1-cent value
		1 dollar = 100 cents
	Idea:
		try to conver the dollar to max-cent value first,
		then conver the reminder to the second-max-cent value,
		and so on.
	It returns a tuple of the combination of the numbers of
		(cent25, cent10, cent5, cent1)
	注意：dollar 是浮点数类型，cent个数为整数类型
	"""
	remainder = int(dollar * 100)
	cent25 = cent10 = cent5 = cent1 = 0

	cent25,remainder = divmod(remainder, 25)
	cent10,remainder = divmod(remainder, 10)
	cent5,remainder  = divmod(remainder, 5)
	cent1 = remainder

	return (cent25, cent10, cent5, cent1)


def main():
	print Dollar2Cents.__doc__
	dollar = float(raw_input('enter the amount of dollar> '))
	print "$%.2f can convert into the minimum number of cents with:" % dollar
	print "cent25(%d), cent10(%d), cent5(%d), cent1(%d)" % Dollar2Cents(dollar)

if __name__ == '__main__':
	main()
