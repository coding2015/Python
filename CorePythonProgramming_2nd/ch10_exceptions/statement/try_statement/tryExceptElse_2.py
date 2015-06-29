try:
    float('er')
except BaseException:
    print 'error'
else:
    print 'continue...'
finally:
    print 'finally'



'''
error
finally
'''
