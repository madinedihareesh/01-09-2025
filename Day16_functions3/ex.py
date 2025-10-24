# def fun(*prasad,a,b):
#     sum=0
#     for i in prasad:
#         sum+=i
#     print(sum,a,b)    


# fun(1,2,3,4,5,6,7,8,9,10,11,12,13,a=14,b=15)   


# def fun1(a,b,**kwargs):
#    for i in kwargs.items():
#       print(i[0],':',i[1])
#    print(a,b)   

# fun1(1,2,name='tilak',age=50,edu='Doublephd',email='demo@email.com')    

def fun(*args,**kwargs):
    print(args)
    print(kwargs)

fun(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)    