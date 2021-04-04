class fenshu:
    def __init__(self,
                 a:int,
                 b:int):
        self.a=a
        self.b=b
        for i in list(range(2,min(a,b)+1)).reserved():
            if self.a%1==0 and self.b%i==0:
                self.a=self.a//i
                self.b=self.b//i
        if self.b==1:
            self=self.a
            del self.b
    def count(self):
        return self.a/self.b
    def __add__(self,num):
        if num==int:
            return fenshu(self.b*num+self.a,self.b)
        elif num==float:
            return self.count()+num
        elif num==fenshu:
            return fenshu(self.a*num.b+num.a*self.b,self.b*num.b)
        else:
            raise ValueError("please input class 'int','float'or'fenshu'")
    def __sub__(self,num):
        if num==int:
            return fenshu(self.a-self.b*num,self.b)
        elif num==float:
            return self.count()-num
        elif num==fenshu:
            return fenshu(self.a*num.b-num.a*self.b,self.b*num.b)
        else:
            raise ValueError("please input class 'int','float'or'fenshu'")
    def __mul__(self,num):
        if num==int:
            return fenshu(self.a*num,self.b)
        elif num==float:
            return self.count()*num
        elif num==fenshu:
            return fenshu(self.a*num.a,self.b*num.b)
        else:
            raise ValueError("please input class 'int','float'or'fenshu'")
    def __truediv__(self,num):
        if num==int:
            return fenshu(self.a,self.b*num)
        elif num==float:
            return self.count()/num
        elif num==fenshu:
            return self.__mul__(fenshu(num.b,num.a))
