#coding:utf8

x = "There are %d types of people." % 10
	#类似print %两边的空格可以任意
binary = "binary"
do_not = "don't"
y = "Thoese who know %s and those who %s." % (binary,  do_not)

print x
print y

print "I said %r." % x
	#%r 输出带单引号
print "numbers:%r,%r" % (1,2)
	#%r 数值类输出不带引号
print "[%%r]I also said:%r." %  y
	#%r 字符串类 输出带双引号
#print "[%%s]I also said:%s." %  y
	#%s 输出不带引号
#print "I also said:\"%s\"."  %  y

hilarious = False
#joke_evaluation = "Isn't that joke so funny?! %s"
joke_evaluation = "Isn't that joke so funny?! %r"	
	#%r 输出无引号
print joke_evaluation % hilarious

w = 'This is the left side of...'
e = "a string with a right side."
#print w e
	#SyntaxError: invalid syntax
print w+e
