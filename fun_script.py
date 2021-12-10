"""
if x even /2
if x odd * 3 +1
"""


def x_cube(x):
    if x % 2 == 0:
        x = x / 2
    else:
        x = (x * 3) + 1

    return x


for i in range(100):
    print(x_cube(x=i))

