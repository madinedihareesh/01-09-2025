# index sort and reverse

l1=[1,2,3,4,5,6,3]
print(l1.index(3,3))

l2=[70,90,20,10,30,40]
l2.sort()
print(l2)
l2.reverse()
print(l2)


l3=['Cat','Dog','Ball','Elephant','Apple','ant']
l3.sort()
print(l3)


# list commprahenssions:
l4=[x for x in range(1,6)]
print(l4)


l5=[x for x in 'python']
print(l5)


# nestedlist:

L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[[3,2,1],[6,5,4],[9,8,7]]
for i in range(len(L1)):
    for j in range(len(L1)):
        print(L1[i][j]+L2[i][j],end=' ')
    print(' ')    