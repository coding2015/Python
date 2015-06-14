#!/usr/bin/python

def Grading(score):
	"""
	Return the grade according to the score.
	"""
	if 90.0 <= score <= 100.0:
		return 'A'
	elif 80.0 <= score <= 89.9:
		return 'B'
	elif 70.0 <= score <= 79.9:
		return 'C'
	elif 60.0 <= score <= 69.9:
		return 'D'
	elif 0.0 <= score <= 59.9:
		return 'F'
	else:
		return 'ValueError:the score is illegal.score[0.0,100.0]'

import operator
def Average(scores):
	sum = reduce(operator.add,scores)
	return sum / len(scores)

def test_average():
	scores = []
	while True:
		score = raw_input('enter a score,"."to end> ')
		if score == '.':
			break
		else:
			scores.append(float(score))
	average = Average(scores)
	print scores
	print 'average:%.1f' % average
	print 'grading:%s' % Grading(average)


def test_grading():
	while True:
		try:
			#score = '%.1f'% float(raw_input('enter a score> ')) #str
			score = float('%.1f'% float(raw_input('enter a score> ')))
		except ValueError:
			print 'ValueError: not a score, please try again.'
		else:
			break
	print score
	print "grading:%s" % Grading(score)


#Entry:
if __name__ == '__main__':
	test_grading()
