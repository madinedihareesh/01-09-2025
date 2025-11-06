import re

'''
match
fullmatch
findall
search
split
group
span
abc
'''

print(re.match('py','python pyhon').span())
print(re.match('py','python pyhon').group())
print(re.match('abc','abcdefghijk').span())
print(re.match('abc','abcdefghijk').group())

pattren=r"python"
text='python is very easy to learn. now a days python plays a vitel role in sw indusry'
print(re.findall(pattren,text))

print(re.search('world','Hi hello world, welcome to my world').group())
print(re.split(' ','Hi hello world, welcome to my world'))


print(re.fullmatch('python','python is very easy o learn'))


'''
+ one or more
* o or more
? zero or one
{m}
{m,n}

[] sets a possible charters
[^....]
.
^[]$
'''

print(re.fullmatch('[!@#$%^&*:;]*','my name is hareesh'))

print(re.fullmatch('^[A-Z]{5}\d{4}[A-Z]{1}$','DYKPM7826M'))

{8,16}