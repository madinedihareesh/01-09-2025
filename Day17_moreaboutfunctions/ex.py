'''
1. Function as Objects
2. Nested Functions
3. passing a functions as a parameter(Higher order function)
4. clouser (Higher order functions)
5. lambda (anonymus function)
6. Decorator
'''
'''
def actual(f):
    print('*'*10)
    f()
    print('*'*10)

def wel():
    print('Welcome to Python') 


actual(wel)


def add(x,y):
    return x+y

def pro(x,y):
    return x*y

def aurthamatic(f,x,y):
    return f(x,y)

print(aurthamatic(add,2,3))
print(aurthamatic(pro,2,3))
'''
'''
def auth(a,b):
    def add():
        print(a+b)
    def pro():
        print(a*b)
    return add(),pro()

auth(5,10) 


sum= lambda x,y: x+y

print(sum(10,5))

print((lambda x,y: x*y)(5,10))
'''

def decorater(f):
    def inner():
        print('+'*10)
        f()
        print('+'*10)
    return inner
def outter(f):
    def inner():
        print('*'* 10)
        f()
        print('*'*10)
    return inner    

@outter
def whish():
    print('welcome')

# whish=outter(whish)
whish()

           