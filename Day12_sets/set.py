'''s={30,20,10,40,60,50}
print(s)
s1=set()
print(s1)
l1=[]
t1=()
s3={}
print(type(s3))
s4=set([1,2,3,4,5,1,2])
print(s4)
s5=set('python')
print(s5)
s6={1,2.5,'python',12+11j}
print(s6)

for x in s:
    print(x)
'''

s={10,20,30,40,50}
s.add(60)
print(s)

s.pop()
print(s)

s.remove(10)
print(s)


# sets in mathamatics
'''
s1={1,2,3,4,5,6,7,8,9,10}
a={1,2,3,4,5}
b={5,7,8,9,10}
c={1,2,3,4,5,6,7,8,9,10}
'''

# sets methods:
A={1,2,3,4,5}
B={4,5,6,7,8}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A|B)
print(A&B)
print(A-B)
print(A^B)


# add()
A.add(6)
print(A)

A.update([7,8,9,10])
print(A)

c=A.copy()
print(c)

c.clear()
print(c)

s={x for x in range(1,6)}
print(s[0])