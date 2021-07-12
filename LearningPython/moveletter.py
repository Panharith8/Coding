# Caesar cipher
text = input("Enter your message: ")
cipher = ''
for char in text:
    #if not char.isalpha():
     #   continue
    char = char.upper()
    code = ord(char) + 2^2
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)