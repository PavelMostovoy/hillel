
status_flag = True

VARIABLE  = 1
processed = "glob"
data = {"initial":"data"}

def function_one(parameter):
    # global VARIABLE
    print("first func")
    processed = f" something with {parameter}"
    VARIABLE = 4
    data = {"key":VARIABLE}
    data["processed"] = processed

    def internal(x):
        nonlocal processed
        print(x.upper()+ processed)

    internal(processed)



function_one("First")


print(data)














