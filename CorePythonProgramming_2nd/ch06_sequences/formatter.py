#coding:utf-8

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
	#输出：1 2 3 4
print formatter % ('one', "two", 'three', "four")
	#输出：'one' 'two' 'three' 'four'
print formatter % (True, False, True, False)
	#输出：True False True False
print formatter % (formatter, formatter, formatter, formatter)
	#输出：'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said good night."
)

