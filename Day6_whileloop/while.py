'''
maximum=0
repcount=int(input('Enter the repetation count:'))
i=0
while i<repcount:
    i+=1
    x=int(input('Enter the value'))
    if x>maximum:
        maximum=x
print(maximum)
'''   

'''
count=0
i=0
number=int(input('ENter the number:'))
while i<number:
    i+=1
    if number%i==0:
        print(i)
        count+=1
print(count)
'''  

# name='Tilak'
# i=0
# while i<len(name):
#     print(name[i])
#     i+=1
'''
name='TulasiPrasad'
voles='AEIOUaeiou'
i=0
while i<len(name):
    if name[i] in voles:
        print('*',end='')
    else:
        print(name[i],end='') 
    i+=1          
'''

'''
*
* *
* * *
* * * * 
* * * * *
'''
# name1='Tulasi'
# name2='Prasad'

# print(name1+name2)


name='Tilak '
print(name*3)

'''
i=5
while i>0:
    
    print('* '*i)
    i-=1


i=0
while i<5:
    i+=1
    print(((5-i)*' ')+'* '*i) 
'''

num=int(input('Enter a number'))
i=0
fact=1
while i<num:
    i+=1
    fact*=i
print(fact)    
