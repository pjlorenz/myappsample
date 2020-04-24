def compute_pay(hours, rate):
    if hours > 40:
        ot_rate = .5 * rate + rate
        return (hours - 40) * ot_rate + 40 * rate

    else:
        return hours * rate

hrs_string = input("Enter hours: ")
rt_string = input("Enter rate: ")
hours1 = float(hrs_string)
rate = float(rt_string)

p = compute_pay(hours1, rate)
print("Total Pay:")
print(p)