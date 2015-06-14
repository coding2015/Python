#coding:utf-8

num = 10
decorate = '*'*num + 'ex%d' + '*'*num

#-----------------ex8：逗号-----------------
title = decorate % 8
print title

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "."*10


end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

#不换行输出，print后跟逗号
#当要print内容过长时，可用逗号‘，’来换行输入
print end1 + end2 + end3 + end4 + end5 + end6,
	#末尾的逗号表示不换行，空格后继续输出下一行
print end7 + end8 + end9 + end10 + end11 + end12

print "hello",
print "Python",
print "!"

print ""

#------------------ex9：三引号---------------
title = decorate % 9
print title

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:",days
print "Here are the months:",months
print "Here are the months:%r" % months
		#输出：'\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug'
		#%r只输出原始数据，不对转义符后内容进行转换

#多行输入并多行输出
#成对三双引号包含所有内容"""xxx"""
print """
There's something on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want,or 5, or 6.
"""

#多行输入但输出一行
print(
"test",
"example",
"is right?"
)
#加‘\n’后仍是只输出一行
print(
	"hello\n",
	"Python\n",
	"how are you today\n"
)
print ""

#-----------------ex10 转义符---------------
title = decorate % 10
print title

#转义单/双引号
print "single quote 'i'" #‘i’
print "double quote -"u"." #u没有打印出来
print "single quote \'i\'" #‘i’
print "double quote -\"u\"." #-"u".
print ""

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'
print ""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\na line."
backslash_cat = "I'm \\ a \\ cat."

#在三引号中可以不对引号转义
#三单引号或三双引号：效果一样
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Ca[nip\n\t* Grass
\t* 'cake'
\t* 'dessert:"chocolate"'
\t* "drinks:'milk'"
\t* "..."
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

quote_escape = "escape single:\'%s\'\rescape double:\"my little %s.\"\n"
print '%%r-:%r' % (quote_escape % ("cat","cat"))
print "%%s-:%s" % (quote_escape % ("dog",'dog'))



#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,

