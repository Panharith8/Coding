'''
dic={"a":"apple","b":"banana","c":"cat","d":"dog"}
print("A for",dic["a"])
'''
'''
fruits={"a":"apple","b":"banana","c":"coconut","d":"durian"}
print("Keys are "+str(fruits.keys()))
print("Content is "+str(fruits.values()))
'''

products=[]

def AddProduct(prod):
    global products
    products.append(prod)

num=int(input("number of product: "))

for i in range(num):
    name=input("name: ")
    model=input("model: ")
    company=input("company: ")
    
    dict={}
    dict.update({"name": name})
    dict.update({"model": model})
    dict.update({"company": company})
    AddProduct(dict)
    
