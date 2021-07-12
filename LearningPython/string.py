def Search(txt,w):
    words=txt.split(" ")
    for word in words:
        if word.lower() == w.lower():
            return True
    return False

def CapWord(txt):
    words=txt.split(" ")
    newWords=[]
    for i in range(len(words)):
        newWords.append(words[i].capitalize())
    return " ".join(newWords)

words="i learn PYTHON language from home."
words2=" Online study "
lWords=words.split(" ")
print("string: ",words)
print("string length: ", len(words))
print("string index 0: ", words[0])
print("string range: ", words[0:7])
print("string Capitalize: ", words.capitalize())
print("string lower case: ", words.lower())
print("string lower case: ", words.upper())
print("string cut space on left:"+words2.lstrip()+">>>")
print("string cut space on left:"+words2.rstrip()+">>>")
print("string cut space on left:"+words2.strip()+">>>")
print("string to list: ", lWords)
print("list to string: ", ",".join(lWords))
print("replace string: ", words.replace("from", "at"))
print("search text: ", Search(words,"lear"))
print("Capital letter: ", CapWord(words))
print("Aasdfsd 2323 werw#$%^&*~234/".isascii())

#chr support value from 0 to 1114111 
print(ord("€"), ord("æ"), ord("I"), ord("i"))

print(chr(29), chr(6016), chr(1114111))

print("chr support value from 0 to 1114111".title() )
print("Chr support valuE from 0 tO 1114111 ".swapcase())
#print(int('0x110000',16))

#IBAN: 000-890-908-789
#palindrome: level kayak mom refer noon rotor moon value