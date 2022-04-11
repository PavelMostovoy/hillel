# with open("example.txt","r") as f:
#     data = f.readlines()
#
# our_data = data[2]
# # **************************
#
# our_data = our_data.strip("[]\n")
# our_data = our_data.split(",")
# our_data = [int(x) for x in our_data]
#
# print(our_data[4]*our_data[-1])
a = [3, "19", 7, 17, "1", 17, 15, 5, 10, 17]
b = [11, 13, 11, 13, 3, 12, (12,17), 1, 17, 4]
c = ["a","f",11,["d",34], {"key":"value", 12: "data"}]
result = (a,b,c)

import json
import yaml


with open("examle.yaml", "w") as f:
    yaml.safe_dump(result,f)


with open("examle.yaml", "r") as f:
    data = yaml.full_load(f)

print(data)