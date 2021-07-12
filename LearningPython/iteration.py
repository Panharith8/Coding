class Switch:
     def __init__(self,n):
           self.__n=n
           self.__i=1
           self.__s=1
     def __iter__(self):
           return self
     def __next__(self):
           self.__i +=1
           if(self.__i > self.__n):
                raise StopIteration
           sum=self.__i + self.__s
           self.__s=sum
           return sum

for i in Switch(5):
      print(i)