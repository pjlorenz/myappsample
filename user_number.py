def user_number():

    user_num = input("Enter a number: Type 'done' when finished.")
    num = int(user_num)
    count = 0
    total = 0
    average = (total + 1) / (count + 1)

    while user_num != "done":

        total = int(user_num) + total
        count += 1
        average = total / count
        # print("Total: " + str(total), "Count: " + str(count), "Average: " + str(average))
        print("Total: {} Count: {} Average: {}".format(total, count, average))
        print("Total: {} Count: {} Average: {}".format(total, count, average))

        user_num = input("Enter a number: ")
        if count >= 7:
            break
             
user_number()
print("Done")