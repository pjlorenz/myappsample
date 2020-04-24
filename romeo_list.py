def romeo():
    fname = open('romeo.txt')

    for line in fname:
        word_list = line.split()
            if len(word_list) > 0:
        return word_list
        # new_list = list(set(word_list))
        # word_list = list(dict.fromkeys(word_list))
        # print(word_list)
        
        # word_list = list(dict.fromkeys(word_list))

    # final = word_list.sort()
    # print(final)
better = romeo()
print(better)