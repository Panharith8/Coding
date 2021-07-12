'''
#n=int(input("Please input Decimal"))
a=5
b=9

print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<1)
print(a<<3)
'''
#Global Variable x can be used for all function
x=10

def sum(a,b):
    return a+b

c=sum(1,2)
print("The total of sum is "+str(c))

def time(a,b):
    return a*b

c=time(2,4)
print("The total of time is "+str(c))

def show():
    x=100
    print(x)

show()
print(x)