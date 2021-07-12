'''
score=int(input("Score="))
if score>=0 and score<=49:
    print("low")
elif score>=50 and score<=65:
    print("Fair")
elif score>=66 and score<=89:
    print("Good")
elif score>=90 and score==100:
    print("Awsome")
else:
    print("Please input score correctly")
'''
'''
income = float(input("Enter the annual income: "))

if income<=0:
    tax=0.0
elif income<85528:
    tax=income*0.18-556.2
elif income>85528:
    tax=14839.2+(income-85528.2)*0.32
tax = round(tax, 0)
print("The tax is:", str(tax), "thalers")
'''