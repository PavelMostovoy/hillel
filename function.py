"""
dd
"""
import random

#
# def demo_function(variable, variable_2=1):
#     """
#     :param variable:
#     :param variable_2:
#     :return: tuple
#     """
#     _ = variable_2
#     result = []
#     for i in variable:
#         result.append(i)
#     return result, "dft"
#
#
# x = demo_function("fgh", 2, )
#
#
#
#
#


# def gen_funct(value):
#     """
#     :param value:
#     :return:
#     """
#     for i in range(value):
#         yield f"iteration {i}"
#         yield "next iteration"
#
#     return "done"
#
#
# var = [k for k in "range(10)"]
#
# var_1 = list()
# for lif in "range(10)":
#     var_1.append(lif)

var_2 = [d for d in "range(10)4"]



def fuu(value):

    if value.isdigit():
        return int(value)
    else:
        return 0



var = list(map(lambda value: int(value) if value.isdigit() else 0, var_2))

var = list(map(fuu, var_2))

print(var)

#
#
# gen = gen_funct(5)
#
# data = [1, 2, 3, 4, 5, 6, 7]
#
# gen2 = (i * 3 for i in data)
#
# a = lambda x: x + 5
#
# for i in gen2:
#     print(i)
#
# print(lambda x: x + 5)
