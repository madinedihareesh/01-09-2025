'''
inner class
class outter:
    def __init__(self):
        self.in_obj=self.inner()

    def display(self):
        in_obj.show()

    class inner:
        def display(self):
           print('inner data')        
'''
'''
class outter:
    def __init__(self):
        self.in_obj=self.inner()

    def display(self):
        self.in_obj.show()

    class inner:
        def show(self):
           print('inner data')

o=outter()
o.display()
'''


'''
Duck typing
method overloading
method overriding
oparator overloading
'''

print(1+2)
print(23.5+89.12)
print('py'+'thon')


print(len([1,2,3,4,5,6]))
print(len({1,2,3,4,5,6,6}))
print(len((1,2,3,4,5,6)))



def add(a,b):
    res=a+b
    print(res)


def add(a,b,c):
    res=a+b+c
    print(res)

add()
