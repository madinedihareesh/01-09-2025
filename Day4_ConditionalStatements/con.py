'''
1.if
2.if else
3.elif
4.nested
5.match

what is your name?

'''

person='non-veg'

if person=='veg':
    print('Serve veg')

age=18


if age>17:
    print('Elligble for vote')


ticket='physical'

if ticket=='physical':
    print('allow')
else:
    print('allow') 


# number=int(input('enter the number:'))

# if number%2==0:
#     print(number, 'is an even number')
# else:
#     print(number,'is a odd number')  


# screen=int(input('Enter the number in between from 1 to 4'))

# if screen==1:
#     print('Original Gang')
# elif (screen==2):
#     print('Hari Hara veramallu')
# elif screen==3:
#     print('sakthi')
# elif screen==4:
#     print('Aghnathavasi') 
# else:
#     print('PLeasae enter a valid number:') 


# marks=int(input('Enter the marks'))

# if marks>=90:
#     print('Grade \'A\'')
# elif marks>=80 and marks<90:
#     print('Grade\'B\'')
# elif marks>=70 and marks<80:
#     print('Grade \'C\'')
# elif marks>=35 and marks<70:
#     print('Grade \'D\'')
# else:
#     print('Fail')                



'''
bill above 2000 then discount is 10%
bill above 3000 then discount is 15%
bill above 5000 then discount is 25%

'''
'''
bill=int(input('Enter the bill amount:'))

if bill>=5000:
    dis=bill*0.25
    print('total',bill-dis)
elif bill>=3000 and bill<5000:
    dis=bill*0.15
    print('total',bill-dis) 
elif bill>=2000 and bill<3000:
    dis=bill*0.1
    print('total',bill-dis)
else:
    print(bill,'discount not available')    
'''

invitation=input('Enter the type of invitaion')

if invitation=='physical' or invitation=='wathsapp':
    print('allowed to the party')
else:
    print('not allowed')    


   