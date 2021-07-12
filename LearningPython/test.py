'''
print("Test")
'''

def I(n):
    s = '+'
    yield s
    
for x in I(2):
    print(x, end='')