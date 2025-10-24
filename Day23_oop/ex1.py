class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print(self.l*self.b)
    
    @staticmethod
    def para(length,breath):
        print(2*length*breath)  

a=Rectangle(10,5)
a.area() 
Rectangle.para(10,5)             