# def fun(a=1,b=2.5,c=[1,2,3,4]):
#     print(a,b,c)

# fun()    

def fun(a,b,c,/,*,d,e):
    print(d,e)

fun(10,20)    