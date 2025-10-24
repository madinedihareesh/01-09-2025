'''
if conditon:
    if condition:
        block of code
    else:
        block of code
else:
   block of code         
'''
'''
status=input('Enter the location')


if status=='reached':
    mode=input('Enter the mode of transport')
    if mode=='metro':
        print('reached home through metro')
    else:
        print('reached home by bus')
else:
    print('still on the way')
'''
'''
year=int(input('Enter a year:'))
if year%400==0:
      print(year)
       
else:
     if year%4==0 and year%100!=0:
        print(year,'is a leap year')
     else:
        print(year,'is not a leap year')
   
'''
# if 1900%4==0:
#     print('2024 is a leap year')
# else:
#     print('not a leap year')    

# passport=input('Enter wether you have your passport or not:')
# if passport=='available':
#     usvisa=input('Enter wether you have visa or not')
#     if usvisa=='available':
#         print('You\'r flying for you edu to US')
#     else:
#         print('you can go to other countries other than us')
# else:
#     print('only esible for domestic') 



# flavor=input('Enter which flavor do you want')
# match flavor:
#     case 'venila':
#         print('This a genral flavor 0f icecream')
#     case 'strawberry':
#         print('This is flavor of icecream usuvally liked by kids')
#     case 'custredapple':
#         print('This is a natural icecream')
#     case 'choco':
#         print('This icecream is made from pure choclets')
#     case _:
#         print('the flavor is not available')                
'''
service=input('Slect the type of service')
Bal=5000
match service:
    case 'diposite':
        amount=int(input('Enter the amount'))
        Avabal=Bal+amount
        print(Avabal)
    case 'withdraw':
        amount=int(input('Enter the amount'))
        Avabal=Bal-amount
        print(Avabal)
    case 'check':
        print(Bal,'amount')
    case _:
        print('Money is not available')        
'''            

year=int(input('ENter the year:'))
if year%100==0:
    if year%400==0:
        print('Leap year')
    else:
        print('not a leap year')
elif year%4==0:
    print('Leap year')
else:
    print('Not leap year')                          