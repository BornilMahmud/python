class myclass:
    x=78
    y=99.77
    v=343/x
    z=v+y


class howto:

    def __init__(self,a ):    # creating constructor
        self.a =a
        
        if a < 20:     # conditional statement
          print("a is gatter than 20 " , a) 

        else :
         print( "a is less than 20  " , a )

obj1 = myclass()   # creating object 1 
print(obj1.v , obj1.x)
print(obj1.z , obj1.y)


obj2 = howto(40)  # creating object 2
print (obj2)