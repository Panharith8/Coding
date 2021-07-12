
'''
boxes = int(input("number of boxs="))
n=1 #count level
height=0 #level number
bNum=0 #number of box per level

while  bNum<=(boxes-n):
    bNum +=n
    n +=1
    height +=1
print("height=", height)

'''
counter=0
n=int(input("N="))
while n>1:   
    counter+=1
    if n%2==1:
        n=n*3+1
        print("f("+str((n-1)/3)+")="+str(n)+"*3+1="+str(n))
    elif n%2==0:
        n=n/2
        print("f("+str(n*2)+")="+str(n)+"/2="+str(n))
#print("Steps="+str(counter))
print("Steps= {}".format(counter))


