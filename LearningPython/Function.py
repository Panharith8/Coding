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
'''
'''
def GetMaxNumber(list,status=True):
    maxNumber=0
    for i in range(len(list)):
        if list[i]>MaxNumber:
            maxNumber==List[i]
    Return maxNumber
    
    
s=GetMaxNumber(list[3,5,7,4])
print(s)
'''
'''
def display(txt):
       if txt=="":
           print("Error input") 
        print(txt)

    s=display("IT step")
    print(s)
'''
'''
def secondConverter(d,h,m,s):
    s1=m*60+h*3600+d*24*3600*60+s
    return s1

s1=secondConverter(1,2,3,4)
print("Total second is "+str(s1))
'''
'''
for i in range(1,6):
    print(i)
'''
'''
def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))
num = 5
print("The factorial of", num, "is", calc_factorial(num))

def Re(x):
    return 
x=5
'''
'''
def triangle(num):
    if num > 0:
        triangle(num-1)
    print(num*str(num))

triangle(6)
'''
'''
def paramid(n,num):
    if (0 == n):
        return
    i=num-n+1
    print(str(i)*i)
    paramid(n-1, num)
    
paramid(8,8)
'''

'''  
def Resome(list[i]):
    if i>0:
        Resome(list[i-1])
        s+=list[i]
    print("The total of the list is "+str(s)+".")

Resum(list[1,2,3])
'''
'''
def triangle(num):
    if num > 0:
        triangle(num-1)
    print(num*str(num))

triangle(6)
'''
'''
def sum(list,n):
    if n<0:
        return 0
    return list[n]+sum(list,n-1)
        
list=[1,2,3]
print("The value is "+str(sum(list,len(list)-1)))

'''
'''
def sum(list,n):
    if n<0:
        return 0
    return list[n]+sum(list,n-1)
        
list=[1,2,3]
print("The value is "+str(sum(list,len(list)-1)))
'''

'''
def Sum(n):
    if len(n)==0:
        return 0
    else:
        return n[0] + Sum(n[1:])

list = [1,2,3]
print("The total value is "+str(Sum(list))+".")
'''

def Allprint(x,n):
    print("allprint n is: {}".format(n))
    if n!=0:
        Allprint(x,n-1)
        Lineprint(x-n)
        Middleprint(n)
        Lineprint(x-n)
        print("\n")
    else: 
        return None

def Lineprint(n):
    #print("lp is:{}".format(n))
    if n!=0:
        Lineprint(n-1)
        print("_",end="")
        #Lineprint(n-1)

def Middleprint(n):
    #print("mp is: {}".format(n))
    if n!=0:
        print(Middleprint(n-1),end="")
        return "* "
    else:
        return " @ "

Allprint(5,5)

'''

def sum(*params):
    for param in params:
        print(param)
sum(1,2,3,4,5)
'''
'''
def display(**params):
    a=len(params)
    for param in params:
        print(params[param])
    print("There are "+str(a)+" items.")

display(name="John",gender="Male",DOB="20-01-1987")
'''
'''
def Allprint(x,n):
    print("allprint n is: {}".format(n))
    if n!=0:
        Allprint(x,n-1)
        Lineprint(x-n)
        Middleprint(n)
        Lineprint(x-n)
        print("\n")
    else: 
        return None

def Lineprint(n):
    #print("lp is:{}".format(n))
    if n!=0:
        Lineprint(n-1)
        print("_",end="")
        #Lineprint(n-1)

def Middleprint(n):
    #print("mp is: {}".format(n))
    if n!=0:
        Middleprint(n-1)
        print(" * ",end="")

Allprint(5,5)
'''