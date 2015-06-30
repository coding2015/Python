'''
there is a limit in recursion depth
'''

#example

def Factorial(n):
    if n > 1:
        return n * Factorial(n-1)
    elif n == 1 or n == 0:
        return 1

'''
test result:
    10! = 3628800
    1000!: RuntimeError:maximum recursion depth exceeded
    原因：递归展开(深度)存在限制
    试验结果：当n>=999时报错
'''
