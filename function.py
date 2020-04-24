
# there's an input to this process. input is number of hours
# there's an output: total pay
# assume they are paid $10/hour
def compute_total_pay(hours):
    #if hours > 40:
     #   return (john_hours - 40) * (1.5 * 10) + (40 * 10)
    #else:
     #   return hours * 10

    hourly_rate = 10
    standard_hours = 40
    overtime_bonus = 1.5
    
    ot_john_pay = (john_hours - standard_hours) * (hourly_rate * overtime_bonus) + (hourly_rate * standard_hours)

    beth_pay = beth_hours * hourly_rate
    john_pay = ot_john_pay
    print("Beth's pay is " + str(beth_pay))
    print("John's pay is " + str(john_pay))
beth_hours = 30
john_hours = 50
hours = beth_hours
compute_total_pay(hours)