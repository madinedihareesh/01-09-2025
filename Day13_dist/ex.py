'''
dict:

'''
s=set()
print(type(s))
d={}
print(type(d))

d1={1:'one',2:'two',3:'three'}
print(d1[1])

d1[4]='four'
print(d1)

d1[3]='thres'
print(d1)

for i in d1:
    print(i)

for i in d1:
    print(d1[i])

l1=[1,2,3,4,5]
l2=['one','two','three','four','five']

L1=[('one','Ace'),(2,'two'),(3,'three'),(4,'four'),(5,'five')]

d2=dict(L1)
print(d2)

d3=dict(zip(l2,l1))
print(d3)


L2=['Ace','tows','thres']
d4=dict(enumerate(L2,start=100))
print(d4)

'''
l1=[x for x in iterbale]
t1=(*(x for x in itrable),)
s1={x for x in iterable}
'''
d5={y:x for x,y in L1}
print(d5)

d6={x:y for x,y in zip(l1,l2)}
print(d6)


d7={x:y for x,y in enumerate(L2,start=10)}
print(d7)

# methods in dict
k=d1.keys()
print(type(k))
for i in k:
    print(i)


v=d1.values()
for i in v:
    print(i)    


item=d1.items()
for i in item:
    print(i) 

# d8=(5,'five')
# d1.update(d8)
# print(d1)   

l3=[1,2,3,4,5]
f=dict.fromkeys(l3,'tulasi')  
print(f)  

d1.pop(2)
print(d1)

d1.popitem()
print(d1)

d1.clear()
print(d1)

del(d1)
print(d1)
