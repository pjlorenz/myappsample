# name is 'bob marley'
#  name.split() = ['bob', 'marley']
# 
# name is 'a great white whale'
# name.split() = ['a', 'great', 'white', 'whale']
def abbrevName(name):
    name_list = name.split()
    first_initial = name_list[0][0]
    last_initial = name_list[1][0]
    initials = first_initial + '.' + last_initial
    return initials

final = abbrevName('Patrick Feeney')
print(final)