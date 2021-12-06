"""
Dock string
"""

su = 0
for variable in range(1, 60):
    # print(variable)
    if variable % 11 == 0:
        print(variable)
        continue
    su += variable
    if su >= 3000:
        break
else:
    print("Filled full")


print(su)
