class Parent:
    def __init__(self):
        pass

    def display(self):
        print('This is a parent class')

class Child(Parent):
    def __init__(self):
        pass
    def show(self):
        print('This a child class')

c=Child()
c.display()  
c.show()


class Reactangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print(self.l*self.b)

class cuboid(Reactangle):
    def __init__(self, l, b,h):
        self.h=h
        super().__init__(l, b)

    def vol(self):
        print(self.l*self.b*self.h)

c=cuboid(10,5,3)
c.vol()
c.area()
print(c.l)



class chirangivee:
    def __init__(self):
        print('This is father')


class ramcharan(chirangivee):
    def __init__(self):
        print('This is son')
        super().__init__() 

R=ramcharan()


'''
Basic
Mupltiple
multilevel
hirarical
'''

class Daddy:
    def skill(self):
        print('He is a good business man')

class Mommy:
    def talent(self):
        print('She is a singer')

class son(Daddy,Mommy):
    def own(self):
        print('He is a good dancer')


s=son()
s.skill()
s.talent()
s.own()


class Grandfather:
    def __init__(self):
        pass
    def head(self):
        print('He is the head of the family')

class Father(Grandfather):
    def __init__(self):
        pass

    def earning(self):
        print('He is the one who earns')

class Grandson(Father):
    def __init__(self):
        pass

    def study(self):
        print('He is studing')


g=Grandson()
g.head()
g.earning()
g.study() 


class Dad:
    def __init__(self):
        pass
    def bussiness(self):
        print('he has a bussiness')

class firstson(Dad):
    def __init__(self):
        pass 

    def Account(self):
        print('He is an account')

class secondson(Dad):
    def __init__(self):
        pass

    def Digi(self):
        print('He is also a digital marketing agent')


f=firstson()
f.bussiness()
f.Account()

s=secondson()
s.Digi()
s.bussiness()
        


