'''
from os import path

def getid():
    if True == path.exists("users.txt"):
        f=open("users.txt","r")
        users=f.readlines()
        f.close()
        if(0 < len(users)):
            lastUser=users[-1]
            userInfo=lastUser.split("||")
            return int(userInfo[0])
    return 1
def adduser(name, gender, dob):
    sid=getid()+1
    sInfo=str(sid)+"||"+name+"||"+gender+"||"+dob+"\n"
    if True == path.exists("users.txt"):
        f=open("users.txt","a")
        f.write(sInfo)
        f.close()
    else:
        f=open("users.txt","w")
        f.write(sInfo)
        f.close()
    '''
file = open("sample.txt", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in file:
  line = line.strip("\n")
  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)

file.close()

print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)