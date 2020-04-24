def loop1():

    for i in range(5):
        print(i)
        # i = i + 1

def loop2():
    word = "hello"
    for c in word:
        print(c)

def loop3(x):
    while x < 8:
        print(x)
        x = x + 1

def loop4(my_list):
    largest = 0
    for i in my_list:
        if i > largest:
            largest = i
    return largest
    

x = loop4([3, 17, 25, 33, 22])
print(x)
# loop3(3)
