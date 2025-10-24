'''
class classname:
    def __init__(self,parametrs):
          parametrs variables declation

    def add(self,a,b):
         a+b   

a=classname()
a.add(10,20)
b=classname()            
'''

class Example:
    owner='Murali Krishna'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Displayname(self):
        print(self.name)

    def Displayage(self):
        print(self.age) 
print(Example.owner)



        