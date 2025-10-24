'''
t1=(1,2,3,4,5)
print(type(t1))

t2=tuple([1,2,3,4,5])
print(t2)

t3=tuple('python')
print(t3)

t4=(3,)
print(type(t4))

print(t1[0])

for x in t1:
    print(x)

# t1[0:0]=6 
print(t1)   

t5=t1[4:0:-1]
print(t5)

t6=t1+t2
print(t6)

t7=t1*3
print(t7)

print(t1!=t2)
'''
'''
t1=(1,2,3,4,5,6)
a,b,c,d,e,f=t1
print(f)
'''

# tuple comprehenssion

t1=(*(x for x in range(1,6)),)
print(t1)

l1=[1,2,3,4,5]
print(sum(l1))

add=0
for x in l1:
    count+=x

print(l1.count())