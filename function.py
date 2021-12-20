"""
dd
"""
import random


def demo_function(variable, variable_2=1):
    _ = variable_2
    result = []
    for i in variable:
        result.append(i)
    return result, "dft"


x = demo_function("fgh", 2, )


def gen_funct(value):
    for i in range(value):
        yield f"iteration {i}"
    return "done"


def foo():
    return 1, 2, 3, 4


a, b, _, _ = foo()


print(a, b, _)
