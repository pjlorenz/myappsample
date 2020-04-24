# you've hard coded inside the function
# we need a general function: takes any list and does this thing to it
def chop(my_list):
    my_list.pop(0)
    my_list.pop(-1)

def chop2(my_list):
    my_list.pop(0)
    my_list.pop(-1)

def middle(input_list):
    list_copy = input_list[:]
    list_copy.pop(0)
    list_copy.pop(-1)
    return list_copy

test_list = [5, 7, 9, 11, 13]
# chop(test_list)
list_final = middle(test_list)
print(list_final, test_list)
