import random

# print(random.random())

# print(random.uniform(10,20))

# print(random.randint(1,6))

# otp=random.randint(1000,9999)

# print('OTP',otp)

# print(random.randrange(10,100,2))

l1=list(range(1,31))

print(l1)

print(random.choice(l1))

print(random.choices(l1,k=3))


random.shuffle(l1)
