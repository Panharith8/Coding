'''
student=[1,"John","Male","20-02-1920",2,"Oscar","Male","1-1-1987"]
title=["ID","Name","Sex","Date of Birth"]

for i in range(len(student)):
    print (title[i],student[i],sep=": ")
'''
'''
studentlist=[[1,"Pov", "male","20-02-1920"],
             [2,"Cheata", "female","20-02-1920"],
             [3,"Sitha", "male","20-02-1920"],
             [4,"Kong", "male","20-02-1920"],
             [5,"Manith", "male","20-02-1920"]
                              ]
#print(studentlist)
for x in studentlist:
    for data in x:
        print(data)
'''
'''
car=['lexus','Rx300','Toyota','2010']
#car[1]='RX400h'
car.append("Brand")
car.insert(3,'Japan')
print(car)
'''
'''
students=[]
m=0
f=0
n=int(input("Please insert number of students="))

for i in range(n):
    element=[]
    element.append(i+1)
    element.append("john"+str(i+1))
    if i%2==0:
        element.append("Male")
        m+=1
    else:
        element.append("Female")
        f+=1
    element.append("John"+str(i+1)+"@test.test")
    students.append(element)

print(students)
print(len(students))

female=0
for student in students:
    for data in student:
        if data=="Female":
            female+=1    
print(female)
#print(m)
#print(f)
'''
'''
list=[]
for i in range(1,101):
    list.append(i)
for i in list:
    if 0==i%2|0==i%3|0==i%7:
        list.remove(i)
print(list)
print("Number="+str(len(list)))
larg=list[0]
for number in list:
    if number>larg:
        larg=number
print(larg)
'''
'''
list1=[1,"a","b"]
#remove by contain
list1.remove("a")
print(list1)
#remove by ID     
del list1[0]
print(list1)
'''
'''
list2=[[1,2,3],["x","y","z"],["a","b","c"]]
#remove by contain 
list2.remove(list2[0])
#remove by ID
del list2[1]
print(list2)
'''
'''
list3=["apple","coconut"]
list3.insert(1,"banana")
print(list3)
'''
'''
# step 1
beatles=[]
print("Step 1:", beatles)
# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step2:", beatles)
# step 3
for i in range(len(beatles),len(beatles)+2):
    n=input("Input Singers=")
    beatles.append(n)
print("Step3:", beatles)
# Step 4
    #print("Value of a: {}".format(a))
for x in range(len(beatles)-1,len(beatles)-3,-1):
    del beatles[x]    
print("Step4:",beatles)
#step 5
beatles.insert(0,"Ringo Starr")
print("Step5:",beatles)
# testing list legth
print("The Fab", len(beatles))
'''
'''
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)
'''
'''
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)
'''
'''
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)
'''
'''
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")
    
'''
'''
myList1 = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
myList=[]
for x in myList1:
    if x not in myList:
        myList.append(x)

print("The list with unique elements only:")
print(myList)
'''
'''
myList = [1, 2, "in", True, "ABC"]
print(1 in myList) # outputs True
print("A" not in myList) # outputs True
print(3 not in myList) # outputs True
print(False in myList) # outputs False
'''
'''
row = []
WHITE_PAWN=["A","B"]
for i in range(8):
    row.append(WHITE_PAWN)
print(row)

WHITE_PAWN=["A","B"]
row = [WHITE_PAWN for i in range(8)]
print(row)
'''
'''
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
rooms[0][4][1] = False
rooms[2][14][10] = True

vacancy = 0
for roomNum in range(20):
    print("Room Number "+ str(roomNum+1) +"  "+str(rooms[2][14][roomNum]))
    if not rooms[2][14][roomNum]:
        vacancy += 1
print(vacancy)
'''
'''
#from sets import Set
lst = [2,4,5,3,2,2,4,6,7]
lst=set(sorted(lst))
print(type(lst))
print(lst)
'''
'''
#from sets import Set
lst = [20,2,4,5,20,3,18,2,2,4,6,7,12]
#lst = sorted(set(lst))
lst = list(set(lst))
lst.sort
print(type(lst))
print(lst)
'''
'''
rooms=[[[True for r in range(10)]for f in range(5)] for b in range(2)]
print(rooms)
'''
# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0]) # outputs: ':('
print(table[0][3]) # outputs: ':)'