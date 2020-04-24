
class Tree:
    def __init__(self, name, height, fruit):
        self.name = name
        self.height = height
        self.fruit = fruit

    def print_fruit(self):
        print(self.fruit)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.name + ': ' + self.fruit


first = Tree("maple", 50, "syrup")
second = Tree("oak", 50, "acorns")
third = Tree("pear", 30, "pears")

# name = ["maple", "oak", "pear"]
# height = [50, 50, 30]
# fruit = ["syrup", "acorns", "pears"]

# mapp = {"Name: " "Maple", "Height: " "50", "Fruit: " "syrup"}
# oaky = {"Name: " "Oak", "Height: " "50", "Fruit: " "acorns"}
# pear = {"Name: " "
# Pear", "Height: " "30", "Fruit: " "pears"}  

# def output(whichtree):
#     print(name[whichtree], height[whichtree], fruit[whichtree])
# print(mapp)

info = first.get_description()
print(info)

