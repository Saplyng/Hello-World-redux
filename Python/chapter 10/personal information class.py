class Person(object):
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    @property
    def lookup(self):
        """see if person exists"""
        return self.name

    @lookup.setter
    def getName(name):
        return name

    def setName(string):
        self.name = name
