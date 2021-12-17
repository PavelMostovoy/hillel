from PlatesList import plates_list

plates = list(set(plates_list))

auto = dict()

marks = ["Ford", "Honda", "Mazda"]

marks.append('Maseraty')

su = len(plates)

part = su // len(marks)

# print(f'overall = {su}   part = {part}')

set_1 = plates[:part]
set_2 = plates[part:part*2]
set_3 = plates[part*2: part*3]
set_4 = plates[part*3:]
data = [set_1, set_2, set_3, set_4]


for i, mark in enumerate(marks):
    # auto[mark] = data[i]
    auto[mark] = plates[part*i: part*(i+1)]



print(auto)
