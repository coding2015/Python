try:
	float('er')
except (ValueError, TypeError), e:
	print 'e:', e



'''
e: could not convert string to float: er

'''
