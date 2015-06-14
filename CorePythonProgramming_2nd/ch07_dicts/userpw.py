#!/usr/bin/python

'''
Example 7.1 in 'core python programming'
This application manages a set of users who
	join the system with a login name and a password.
Onec established, existing users can return as ling as they remember their login and password. New users cannot create an entry with someone else's login name.
'''

db = {}

import time
def newuser():
	prompt = 'login desired: '
	while True:
		name = raw_input(prompt)
		if name in db:
			prompt = 'name taken, try another: '
			continue
		else:
			break
	pwd = raw_input('password: ')
	db[name] = {'pwd':pwd}
	db[name]['timestamp'] = time.time()


def olduser():
	name = raw_input('login: ')
	if name not in db:
		print 'Login failed: username does not exist.'
		return
	pwd = raw_input('passwd: ')
	passwd = db.get(name)['pwd']

	if passwd == pwd:
		print 'Welcome back', name
		curtime = time.time()
		timestamp = db.get(name)['timestamp']
		intervals = timestamp - time.time()
		if intervals/60 < 4:
			print 'You already logged in at:<last_login_%s>' % time.ctime(timestamp)
		db[name]['timestamp'] = curtime
	else:
		print 'Login failed: password incorrect '


def delete_user():
	name = raw_input('user name: ')
	if name not in db:
		print name, 'dose not exist.'
	else:
		del db[name]	

def show_all():
	print 'user list'.center(50)
	print 'num'.rjust(4),'user'.center(20),'password'.center(20),'logintime'.center(10)
	print 
	i = 1
	for user in sorted(db.iterkeys()):
		print ('%d'% i).rjust(4),user.center(20), db[user]['pwd'].center(20),time.ctime(db[user]['timestamp'])	
		i += 1

CMDs = {'q':None,'n':newuser,'e':olduser,'d':delete_user,'s':show_all}

def showmenu():
	prompt = '''
(N)ew User Login
(E)xisting User Login
(D)elete a user
(s)how all users
(Q)uit

Enter choice: '''
	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (EOFError, KeyboardInterrupt):
				choice = 'q'
			print '\nYou Picked: [%s]' % choice
			if choice not in CMDs:
				print 'invaild option, try again'
			else:
				chosen = True
		
		if choice == 'q': done = True
		else:
			CMDs[choice]()
		#if choice == 'n': newuser()
		#if choice == 'e': olduser()

if __name__ == '__main__':
		showmenu()
			
	
