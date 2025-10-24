'''
syntax:
for element in squental data type
for i in range(start,stop,step)
range(5)ending value
range(1,5)starting and ending value

i=10
while i>0:
print(i)
    i-=1
'''
# for i in range(1,11,1):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# a=0
# b=1
# for i in range(1,16):
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c

for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,'is a prime number')        


for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print('* ',end='')
    print('')        