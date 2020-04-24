
try:

    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter rate:")
    r = float(rate)
    otime = h - 40
    pay = (h - otime) * r
    otpay = otime * 15.75

    if h > 40:
        print(otpay + pay)

    else:
        print(pay)

except:
    print("Error: please enter a number for hours and rate.")
