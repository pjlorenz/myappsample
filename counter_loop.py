def counter_loop(string, letter):

    
    count = 0 
    for letter in string:
        if letter == "s":
            count = count + 1

    print(count)

counter_loop("sassafras", "s")
print("Hello world")


