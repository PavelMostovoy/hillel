

class PlateNumber():
    def __init__(self, region, number, extension, db):
        self.number = number
        self.region = region
        self.extension = extension
        self.db = db

    def calculate_number(self):
        return self.number

    def is_unique(self):
        if self.region + self.number +self.extension in  self.db:
            return "exist"
        else:
            return "not in list"


v1 = PlateNumber("aa", "0987", "nn", "fake")

print(v1.calculate_number())

class PlateWithOwher(PlateNumber):

    def get_owner(self):
        print("not implemented")

v3 = PlateWithOwher("d","dddd","dd","ddd")

v3.get_owner()