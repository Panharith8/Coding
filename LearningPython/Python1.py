x=int(input("x="))
if((x%3==0) | (x%5==0) | (x%7==0)):
    print("The number can divide by 3,5,7")
elif((x%2==0) | (x%4==0) | (x%6==0)):
     print("The number can divide by 2,4,6")   
else:
    print("0")