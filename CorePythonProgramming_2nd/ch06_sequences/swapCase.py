#!/usr/bin/python
'''
Exercise 6-10:
	Implement the str's BIF: swapcase()
	return a new string of case-inverted to the input string

Problem-Solved:
	str is an unchagable type
	so how to record every charater's convert?
	and transfer the records into string in the end? 
Solving:
	use ''.join(seq):
		record the new charater in a list
		and in the end use ''.join(list) to join the charater-item of list together 

KeyPoint:
	str.join()
	only letter has upper/lower case
'''

def SwapCase(old_str):
	new_list = []
	for c in old_str:
		if c.isalnum() and not c.isdigit(): #convert letter only
			if c.isupper():
				new_list.append(c.lower())
			else:
				new_list.append(c.upper())
		else:
			new_list.append(c)
	
	new_str = ''.join(new_list)	#convert character-list to a string

	return new_str


def main():
	s = ['Mr.White','WHI TE','white','123*Wh_Ite#--!&%']
	for eachStr in s :
		print
		print 'orin:',eachStr
		print 'SwapCase():',SwapCase(eachStr)
		print 'str.swap():',eachStr.swapcase()
	print

if __name__ == '__main__':
	main()
