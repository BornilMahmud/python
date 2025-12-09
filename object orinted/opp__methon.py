class bornil():
    name = "Bornil Mahmud " # attribute
    age = 21             # attribute
    favorite = "one piece"   # attribute


    def info(self,a,b):   # method with parameters
        print( "My name is " , self.name)
        print( " My age is " , self.age )
        print( " My fovorite anime is " , self.favorite)
        print ( " i know some one named ", a , " who is " ,b , " years old  ") 


    def information (self):     # method without parameters
        self.info("shovo ", 22 )

obj1 =bornil()   # creating object
obj1.info("sabit",23)       # calling method with parameters
obj1.information()   # calling method without parameters
