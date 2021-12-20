from PlatesList import plates_list

plates = list(set(plates_list))

auto = dict()

marks = ["Ford", "Honda", "Mazda"]

marks.append('Maseraty')
marks.append('BMW')
marks.append('Opel')


su = len(plates)

part = su // len(marks)

for i, mark in enumerate(marks):
    auto[mark] = dict()
    auto[mark]['plates'] = []
    for x in range(1, part):
        auto[mark]['plates'].append(plates.pop())


print(auto)
