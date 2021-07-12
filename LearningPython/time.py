'''
import time

for i in range(1,6):
    print(str(i)+" Mississippi")
    time.sleep(4)

print("Ready Go!")
'''
'''
largestNumber = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largestNumber:
        largestNumber = number

if counter != 0:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")
'''
'''
largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:    
    number = int(input("Enter a number or type -1 to end program: "))
    
    if number == -1:
        continue
    counter += 1
    
    if number > largestNumber:
        largestNumber = number
if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

'''
'''
# Prompt the user to enter a word
n=input("Please input a word for vowel eater=")
# and assign it to the userWord variable.
userWord=n.upper()
for letter in userWord:
    # Complete the body of the for loop.
    if letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
        continue
    print(letter)
'''
'''
wordWithoutVovels = ""
# Prompt the user to enter a word
n=input("Please input a word=")
# and assign it to the userWord variable
userWord=n.upper()
for letter in userWord:
    # Complete the body of the loop.
    if letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
        continue
    else:
        wordWithoutVovels+=letter
# Print the word assigned to wordWithoutVowels.
print("Word without vowels:"+str(wordWithoutVovels))
'''