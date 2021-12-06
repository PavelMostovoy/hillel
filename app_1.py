"""
if x even /2
if x odd * 3 +1
"""
# print("In case of filling '0' programm will end")

x = False
while True:

    x = int(input("Please input number :  " if x else
                  "In case of filling '0'"
                  " program will end \nPlease input number :  "))
    if x == 0:
        break
    elif x < 0:
        print("Should be positive only ")
        x = abs(x)
    i = 0
    while x != 1:
        i = i + 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = (x * 3) + 1

    print(f"Number of cycles {i}")

