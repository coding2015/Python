def f():
    while True:
        try:
            break
        finally:
            print 'finally'
                          
 
>>> f()
finally




