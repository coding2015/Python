#!/usr/bin/python
#coding:utf-8
'''
rochambeau:石头剪刀布
用户触发一个随机项，程序给出对应项（赢/平手）
随机数0-3对应石头剪刀布，石头剪刀布对应策略函数
'''
Roch = ('Paper','Rock','Scissors')

import random
def Paper():
	return random.choice((Roch[0],Roch[2]))

def Rock():
	return random.choice((Roch[1],Roch[0]))

def Scissors():
	return random.choice((Roch[2],Roch[1]))

Strategy = {'Paper':Paper, 'Rock':Rock, 'Scissors':Scissors}

def main():
	'''
	Rochambeau:press any keyboard, it will produce a rochambeau
	which represent your's choice, and the process will simultaneously 
	produce it's choice.
	'''
	while True:
		try:
			raw_input('press any key to generate a rochambeau> ...')
		except (KeyboardInterrupt,EOFError):	
			print	
			break
		else:
			c = random.randint(0,2)
			print 'your choice:', Roch[c]
			print 'my choice:',Strategy[Roch[c]]()


if __name__ == '__main__':
	main()
