
def addSomeNumbers():
    sum = 0
    for m in range(1, 11, 2):
        # print (m)
        sum = sum + m
    return sum

def loop2(data):
    '''data must be a list'''

    for i in data:
        if i > 9:
            print(i)


loop2([1, 4, 6, 7, 10, 15, 17, 23])



# the result is the sum of 0 + 1 + 2 + 3 + 4

#    m           sum
#    0            0    <- entering the first time
#                 0    <-  during the loop
#    1                 <- entering the second time
#                 1    <- during the loop
#    2                 <- entering the third time
#                 3    <- during the loop
#    3                 <- entering the fourth time
#                 6    <- during the loop
#    4                 <- entering the fifth time
#                 10   <- during the loop
                     