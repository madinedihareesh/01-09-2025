'''
l1=[1,2,3,4,5]
l2=[1.2,2.5,3.4,4.3,5.6]
l3=[10+3j,20+11j]
l4=['peter','parker','bruce','clarck']

l=[1,2.5,23+11j,'string',True]
print(len(l1))

L1=list('Python')
print(L1)
L2=list((1,2,3,4,5))
print(L2)

L3=[]
print(type(L3))

for i in l1:
    print(i)


l1[0:0]=[6]
print(l1)  

l1[9:9]=[7]
print(l1)

l1[3:3]=[8,9,10]
print(l1)

l1[3:0:-1]=[11,12,13]
print(l1)
'''

# List concatination and repetation
'''
l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)
l4=l1*3
print(l4)
'''

# list comarission
'''
l1=[1,2,3]
l2=[1,2,3,4]
print(l1==l2)
print(l1!=l2)
print(l2>l1)
'''

# adding elements to the list
l1=[1,2,3]
l1.append(4)
print(l1)

l2=[5,6,7]
l1.extend(l2)
print(l1)

l1.insert(1,8)
print(l1)

# removing elements from the list
l1.pop()
print(l1)
l1.remove(8)
print(l1)

l1.clear()
print(l1)

del(l1)
print(l1)