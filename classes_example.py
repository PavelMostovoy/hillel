class PlateNumber:
    colors = ["Red", "Green", "Blue"]
    marks = ["Audi", "Toyota", "Bentley"]

    def __init__(self, region, number, extension, db):
        self.__number = number
        self.__region = region
        self.__extension = extension
        self.__db = db
        self.__color = None
        self.__year = int()
        self.__mark = "Audi"

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, data):
        self.__year = int(data)

    def set_color(self, data):
        if data in self.colors:
            self.__color = data
        else:
            color = input("Incorrect color please fill correct :")
            self.set_color(color)

    def color(self):
        return self.__color

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, data):
        if data in self.marks:
            self.__mark = data
        else:
            mark = input("Incorrect mark please fill correct :")
            self.mark = mark

    def calculate_number(self):
        return self.__number

    def is_unique(self):
        if self.__region + self.__number + self.__extension in self.db:
            return "exist"
        else:
            return "not in list"


class Plates80(PlateNumber):
    def __init__(self, region, number, extension, db):
        super().__init__(region, number, extension, db)
        self.__year = 1980

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, data):
        if int(data) == 2017:
            super().set_color(input("Enter color"))
        if int(data) != 1980:
            self.__year = 1980

    def set_color(self, data):
        if data in self.colors:
            self.__color = data
        else:
            self.__color = "Grey"

    def color(self):
        return self.__color


a1 = Plates80("AA", "0000", "BB", "None")


a1.set_color("Black")

a1.year = 2017

print(a1.color())

