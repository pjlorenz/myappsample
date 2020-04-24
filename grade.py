
try:
    score = input("Enter Score: ")
    inScore = float(score)

    if inScore > 1.0 or inScore < 0.0:
        print("Enter a proper score between 0.0 and 1.0")

    elif inScore >= 0.9 and inScore <= 1.0:
        print("A")
    elif inScore >= 0.8:
        print("B")
    elif inScore >= 0.7:
        print("C")
    elif inScore >= 0.6:
        print("D")
    elif inScore < 0.6 and inScore >= 0:
        print("F")

except:
    print("Error: please enter a proper score.")
    

