

def demo(x,y):
    return x+y

def func(a,b):
    try:
        res = a/b
        print(f"\n {res} \n")
        xx = demo(a, b)
        print(xx)
    except (ZeroDivisionError, TypeError, SyntaxError):
        print('error')

func(5,7)

a = None
if not a or sum(a)==0.0:
    print('a is empty or nothig inside or it is None')

else:
    print('not_empty')
    