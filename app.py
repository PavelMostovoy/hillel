# var = 10
# print(var)
import time
VARIABLE = "Global"


def new_func(x: int, y: int):
    var = input("fill something = > ")
    var_1 = int(var)
    var_2 = var_1 + x + y
    if var_2 > 20:
        return f'output value = {var_2}, input value = {var}'
    else:
        return False


print(new_func(100, 34))

