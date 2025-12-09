class Bornil():
    x=8    # class variable   both are same 
    y=9    # static variable  

    def addition(self): #  both are same normal methon and instance method
        sum = self.x +self.y
        print("The sum of x and y is :  ", sum)


    @staticmethod  # decorator for static method
    def static_method():
        sum = Bornil.x + Bornil.y 
        print( " THe sun of x snd y using static method is :  ", sum )


obj= Bornil()# creating object
obj.addition()# calling normal method using object
obj.static_method() # calling static method using object

Bornil.static_method() # calling static method using class name
print(Bornil.x)  # printing class variable using class name
print(Bornil.y)  # printing static variable using class name