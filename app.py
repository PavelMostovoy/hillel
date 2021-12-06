"""
Dock string
"""

var = """
Понятие цикла.
Циклические алгоритмы
Конструкция while
Ключевые слова break и continue
Конструкция while - else
Примеры использования цикла while
"""


for i, variable in enumerate(var):
    if variable == "w":
        print(f"found in {i}")
    if variable == "b":
        print(f"found in {i}")

