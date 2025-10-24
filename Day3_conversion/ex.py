'''

'''
a=20
print(bin(a))
print(a)
print(oct(a))
print(hex(a))

# type:
'''
int
float
complex
bool
string
'''
print(int(0b10100))
print(int(12.78))
# print(int(12+3j))an integer cannot convert a complex number
print(int(True))
print(int(False))
print(int('10'))

print(float(10))
# print(float(12+3j))
print(float(True))
print(float('12.59'))

print(complex(10))
print(complex(12.39))
print(complex(True))
print(complex('10'))

print(bool(''))

print(str(10))
print(str(10+0j))
print(type(str(True)))
print(str(10.54))