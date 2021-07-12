'''
for i in range(100):
   print(i)
'''
'''
even=""
odd=""
x=int(input("Please input x="))

for i in range(x):
    if(0==(i%2)):
        #even=even+i
        #print(even,end=",")
        even+=str(i)+","       
    elif(0!=(i%2)):
        #odd=odd+i
        #print(odd,end=",")
        odd+=str(i)+"," 
print("\nTotal even number="+str(even))
print("Total odd number="+str(odd))
'''
'''
#2nd way
x=1
z=""
for x in range(1,10,2):
    z+=str(x)+","
print(z)
    
'''
'''

#3rd way
h=0
for g in range(1,51):
    if g%3==0 and g%7==0:
        h=h+1
print(h)
'''
'''
x=0
i=int(input("Please input x="))
while x<10:
    x+=1
    print(str(i)+" x "+str(x)+" = "+str(x*i))
'''
'''
txt="Cambodia"
for i in txt:
    print(i)
'''
'''
x=int(input("Input x(Max=300)="))
for i in range(1,x):
    if (i%2==0) and (i%3==0) and (i%5==0):
        print(i)
    if i>300:
        break
 '''
'''
for i in range(1,21):
    if (i%5==0):   
        continue
    print(i)
'''
'''
list=[1,2,3,4,5,6,7]
for i in list:
    print(i)     
'''
'''
list=["a","b","c","d"]
for i in range(len(list)):
    print(list[i])
print(len(list))
print(list[3])
'''
'''
list=["banana","apple","orange","cherry","strawbery"]
for i in range(len(list)):
    if list[i]=="orange":
        print(list[i]+" is at index "+str(i)+".")
        break
'''
'''

secret_number = 777
n=int(input("Please input the secret number: "))
while n!=secret_number:
    print("Ha ha! You're stuck in my loop")
    n=int(input("Please input the secret number: "))
else:
    print("Well done, muggle! you are free now.")

 '''       

  