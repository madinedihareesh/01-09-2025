name='AchiversIT'

'''
spliciing:
[start:end:step]
'''
print(name[0:3:2])
print(name[::-1])
print(name[4:])

'''
string repetation(*):

'''
print(name*3)

'''
string concatination(+):

'''
title='Tulasi'
title1='Prasad'
print(title+title1)


'''
string compassions:
>,<,<=,>=,==,!=
0-9,A-Z,a-z
'''

print('tulasi'<'tilak')

ex='I am learing python and it is very easy to learn'
ex1='can can a can is a cancer'
print(ex.find('python',14))
print(ex.find('to'))
print(ex.rfind('to'))
print(ex.index('to'))
print(ex.rindex('to'))
print(ex1.count('can'))

# Alingment and padding
name1='Tilak'
test=name1.rjust(10,' ')
test1=name1.ljust(10,' ')
test2='   hello   '
print(name1.ljust(10,'*'))
print(name1.rjust(10,'*'))
print(name1.center(15,'*'))
print(name1.zfill(15))
print(test.lstrip())
print(test1.rstrip())
print(test2.strip())