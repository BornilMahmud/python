class father() :
    a=89
    b=57
    

    def __init__(self,x,y):
        self.x=x
        self.y=y
        total =self.a + self.b
        print("The number is printed is : ", total)

    def sumation(self):
        print("the methond is working ", self.a * self.b)
    
class mother():
    b=89
    v=890

    def __init__(self,mm,u):
        self.mm=mm
        self.u=u


    def sub(self):
        print ("subtracting B and V : ",self.b-self.v)



class son (father,mother):
    def __init__(self,x,y,mm,u):
        father.__init__(self,x,y)
        mother.__init__(self,mm,u)


    

obj= son(7,8,9,3)
obj.sub()
obj.sumation()


