def computepay(my_hours, my_rate):
    '''my_hours is number of hours they worked
       my_rate is standard rate per hour 

       computepay() computes the week's pay given number of hours worked
       and standard rate
    '''
    if my_hours > 40:
        ot_rate = .5 * my_rate + my_rate
        return (my_hours - 40) * ot_rate + 40 * my_rate
    else:
        return my_hours * my_rate
    
hrs_string = input("Enter Hours: ")
rate_string = input("Enter Rate: ")
hours = float(hrs_string)
#standard_hours = 40
rate = float(rate_string)

#ot_hrs = float_hrs - standard_hours
#ot_rate = standard_rate + (.5 * standard_rate)

p = computepay(hours, rate)
print("Pay",p)