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

gen = gen_funct(5)

for i in gen:
    print(i)