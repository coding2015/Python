"递归函数的参数不能设置默认值"
why?

def hanoi(a='A',b='B',c='C',n): #递归函数的参数不能设置默认值
    "move n plates from A seat to C seat by B seat"
    if n>1:
        hanoi(a,c,b,n-1)
        move(a,c,n)
        hanoi(b,a,c,n-1)
    else:
        move(a,c,n)

>>>
    def hanoi(a='A',b='B',c='C',n):
SyntaxError: non-default argument follows default argument



