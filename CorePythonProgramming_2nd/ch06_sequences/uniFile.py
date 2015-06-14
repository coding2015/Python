'''
	A test of encoding and decoding unicode from file
'''
#/usr/bin/python

FILE = 'uniFile.txt'
CODEC = 'utf-8'

uni_out = u'hello python \u1120\u2345'
bytes_out = uni_out.encode(CODEC)

print uni_out, bytes_out
print 'types:',type(uni_out),type(bytes_out)


fobj = open(FILE,'w')
fobj.write(bytes_out)
fobj.close()

fobj = open(FILE,'r')
bytes_in = fobj.read()
fobj.close()
uni_in = bytes_in.decode(CODEC)

print 'types:',type(uni_in),type(bytes_in)
print uni_in, bytes_in

