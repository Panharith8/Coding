class car:
    brand=""
    sery=""
    number=None

    __id=None

    def __init__(self,i,b,s,n):
        self.__id=i
        self.brand=b
        self.sery=s
        self.number=n

    def printSery(self):
        return self.brand+" "+self.sery+" "+self.number