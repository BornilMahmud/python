class myclass:
      x=8
      r =6
      
      def __init__ (self,a ,b):      # constructor 
         self.a=a;      ###   constructor with parameters
         self.b=b;       ###   instance variable
         sum = self.x + self.r +a+b
         print("this is how constructor works " )
         print( sum , a , b )

      def display(self):
          print( " this is how methon works intance variable a and b are : " , self.a , self.b ) ## instance method


obj =myclass(10,39)
obj.display()




