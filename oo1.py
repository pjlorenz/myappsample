
name = ["Mike", "Pat"]
age = [51, 49]
zip_code = [91101, 45218]

mike1 = ["Mike", 51, 91101]
pat1 = ["Pat", 49, 45218]

mike = {'name': 'Mike', 'age': 51, 'zip_code': 91101}
pat = {'name': 'Pat', 'age': 49, 'zip_code': 45218}

class Person:
    def __init__(self, name, age, zip_code):
        self.name = name
        self.age = age
        self.zip_code = zip_code

    def output(self):
        print('Name: {} Age: {} Zip code: {}'.format(self.name, self.age, self.zip_code))


def output(whichGuy):    
    #(name, age, zip_code)
    print(name[whichGuy], age[whichGuy], zip_code[whichGuy])

#output()
print(mike)

mikeObject = Person('Mike', 51, 91101)
mikeObject.output()

class Dog:

    def bark():
        pass

    def output():
        pass
