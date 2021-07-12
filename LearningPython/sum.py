'''
m=int(input("Please in put n="))
def sum(n):
    s= 0
    i=0
    while i <= n:
        s = s + i
        i+=1
    return s
a=sum(m)
print(a)
'''
def Sum(n):
    result=0
    for i in range(1,n+1):
        result +=i
    return result
x=Sum(int(input("Input X: ")))
print("result: "+str(x))