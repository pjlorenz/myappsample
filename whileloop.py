def user_input():

    myInput = input("Type a word:")
    while myInput != "stop":
        print(myInput)
        myInput = input("Type a word:")

def loop2():

    # for i in range(12):
    #     print(i)

    i = 1
    while i < 100:
        print(i)
        i = i + i * i
    
#    i
#   1   ->  2
#   2   ->  6
#   6   ->  42
#   42  ->  1800
    

# user_input()
loop2()
