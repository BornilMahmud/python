class father :
    c=8
    f=90
     

    def add(self):
        print(self.c+self.f)

    def sub(self):
        print(self.c-self.f)

class son(father) :
    pass


obj=son()
obj.add()
obj.sub()

