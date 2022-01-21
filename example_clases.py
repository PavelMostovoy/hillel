

class ToyClass:
    var = 17

    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        cls.value_01 = 17
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


a = ToyClass()
a.value = "some value"

print(dir(a))


print(dir(ToyClass))

a.classmethod()

print(dir(a))
print(dir(ToyClass))