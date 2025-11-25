In_Hours=input("Enter Hours: ")
In_Rate=input("Enter Rate: ")
hours=float(In_Hours)
rate=float(In_Rate)
def computepay():
    pay_=((hours//10)*10)*10+(hours%10)*15
    pay=float(pay_)
    print("Pay:",pay)
computepay()