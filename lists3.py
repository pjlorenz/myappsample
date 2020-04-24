def learn_lists(my_list):
    my_list.pop(1)
    my_list.pop(1)

#   if you want to delete (pop) two numbers in a row, then use same index number twice
test_list = [8, 12, 15, 22, 11]
learn_lists(test_list)
print(test_list)