
'''
a=12
b="5"
try:
    z=a/int(b)
    print(z)
except:print("Catch error")
'''
'''
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")
print("THE END.")
'''
'''
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")
print("THE END.")
'''
'''
def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return "Error"

print(badFun(0))
print("THE END.")
'''
'''
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")
'''
'''
def badFun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise
try:
    badFun(0)
except ArithmeticError:
    print("I see!")
print("THE END.")
'''


'''import math
x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
'''
'''
list = [1, 2, 3, 4, 5]
ix = 0
doit = True
while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False
print('Done')
'''

ddef readint(prompt, min, max):
    try:
        v=int(input(prompt))
        assert v>=min and v<=max,"The value is not within permitted range(min..max)"
        return v
    except ValueError:
        print("Wrong input")

v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)


