"""
dd
"""
li = []

def outer(fun):
    """
    """
    def inner(*args):

        print("Resultat equal to :")
        ret = fun(*args)
        print("meters")
        return ret

    return inner



@outer
def boo() -> int:
    global li
    li.append("iteration")
    print("another function")
    return 1


# a = boo()

@outer
def func(a,b):
    return a+b


@outer
def func_1(x,y,z):
    print (x**2+y**2+z**2)


func_1(2,5,8)


from functools import partial

def my_function(a="",b=""):
    print(f"{a=}, b{b=}")

my_function_foo = partial(my_function, b='bar')


my_function_foo("old")