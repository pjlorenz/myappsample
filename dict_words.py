# new model of functions. normally we don't know what happens inside the 7-11,
# and any data taht comes back out is new data not affecting any old data

def addSeven(x):
    x = 7 + x
    return x

def addToList(x):
    x.append(3)
    

a = [1, 2, 3, 4]
addToList(a)
print(a)



# 
#
#      ----7/11---------
#      |1-> x           |
#      |  1             |
#      |  8             |
#      | -return 8---------------->
#      ------------------
#
#  line number |  x  |   b
#  4            n/a     n/a
#  8              1      n/a
#  9 ---> go into a function -> the value 1 (don't pass variable!!!)
#                         8
#
# when we call a function with a list, it behaves differently.



def make_dict():

    word_dict = dict()
    fhand = open('words.txt')
    
    for i in fhand:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] = word_dict[i] + 1
        
    print(word_dict)
# make_dict()
