class father:
    bike ="motorcycle"
    home = "rent"

    def __init__(self,me):
        self.me=me
        print( me ,f" is taking {self.bike} and going to collect {self.home}")

    def takemoney(self,me):
        print( "Take money who ever needed " , me) 

class elderson(father):
    def __init__(self,me):
        father.__init__(self,me)

class youngson(father):
    def __init__(self,me):
        father.__init__(self,me)

# using elderson class
obj1=elderson("shahid")
obj1.takemoney(200)

# using youngson class 
obj2=youngson("bornil")
obj2.takemoney(500)