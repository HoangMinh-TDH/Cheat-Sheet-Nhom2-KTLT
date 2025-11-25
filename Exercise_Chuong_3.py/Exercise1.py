a=input("Enter Hours: ")
b=input("Enter Rate: ")
hours=float(a)
rate=float(b)
if hours<=40:
    pay=hours*rate
elif hours>40:
    pay=40*rate+(hours-40)*(rate*1.5)
print("Pay:",pay)