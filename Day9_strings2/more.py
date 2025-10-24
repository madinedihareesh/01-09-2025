# joins and splits

# replace:
s1='a-b-c-d'
print(s1.replace('-','*'))

# join
s2='/'
s3='abc'
s4=s2.join(s3)
print(s4)

# split
sen='hi my name is john'
print(sen.split(' ',1))

# rsplit
print(sen.rsplit(' ',1))

# splictlines:
para='''HI
how are you doing
i am doing fine'''
print(para.splitlines())

# prefix and sufix:

# sartswith:
intro='python is very easy to learn'
print(intro.startswith('python'))
# endswith
print(intro.endswith('learn'))
# remove sufix
print(intro.removesuffix('learn'))
# remove prefix:
print(intro.removeprefix('py'))

# partitions:
email='demo@gmail.com'
print(email.partition('@'))

# upper():
data='achiversit'
print(data.upper())

# lower()
data1='ACHIEVERSIT'
print(data1.lower())

# title():
data2='hello world'
print(data2.title())

# captalize:
print(data2.capitalize())

# swapcase():
s='AcHiEvErSiT'
print(s.swapcase())
print(s.casefold())

f=12.59
print(isinstance(f,float))