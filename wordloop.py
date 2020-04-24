def word_loop():
    # 0 to 9 . how many in the list 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    #
    word = "absolutely"

    for i in range(len(word)):
        # we don't want to hardcode 9... we want it to work with any string word
        # len(word) is 10 <-- that's a clue
        print(word[len(word) - 1 - i])

    
        
    # i      what character do you want to print?  9 - i
    # 0      y            9                         9
    # 1      l            8                         8
    # 2      e            7
    #...
    # 9

    index = 1
    while index <= len(word):
        letter = word[-index]
        print(letter)
        index = index + 1

    index = 0
    while index < len(word):
        newIndex = len(word) - index - 1
        print(word[newIndex])
        index += 1

    


# index    -index    word[-index]
#   1         -1            y
#   2         -2            l
# ...
#   9         -9            b
#   10        -10           a


#  index      len(word) - index - 1
#   0             9
#   1             8
#   2             7
#  ...
#   9             0      
#   10  stop 
    

# someList = [1, 2, 3, 4]
# someList[-2]

def func2():
    word = "fabulous"
    for i in range(len(word) - 1, -1, -1):
        print(word[i])

func2()