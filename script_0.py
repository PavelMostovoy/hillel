# value_tuple = (0, 1, 2, 10, 3, 6, 12, 3, 1, 100, 12, 34, 3, "a", "b", "b")
#
# value_list = [0, 1, 2, 10, 3, 6, 12, 3, 1, value_tuple, 100, 12, 34, 3,
# "a", "b", "b"]
#
# value_set = {0, 1, 2, 3, 3, value_tuple}
#
value_set_1 = (0, 1, 2, 10, 3, 6, 12, 3, 1, 100, 12, 34, 3, "a", "b", "b")
#
# value_set.add(value_list)
#
#
# print(value_set)
#

import random

# x = int(random.randint(10, 100))


var = list()

for i in range(10):
    var.append(random.randint(10, 100))

print(var)

var_1 = [i*2 for i in value_set_1]

print(var_1)