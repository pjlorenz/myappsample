def learn_list(my_list):
    my_list.pop(0)
    my_list.pop(-1)

test_list = [5, 7, 9, 11, 13]
learn_list(test_list)
new_list = test_list + test_list
print(new_list)