'break in try-block'

def f():
    while True:
        try:
            break
        finally:
            print 'finally'
                          
 
>>> f()
finally




