def num(n):
    for i in range(n):
        yield i
    for i in num(10):
        print(i)

nm=num(3)
print(next(nm))    
print(next(nm))   
print(next(nm))   
    