#!/usr/bin/python

'Exercise 10-8'


def safe_input():
	try:
		data = raw_input('> ')
	except (EOFError, KeyboardInterrupt):
		data = None
	return data
