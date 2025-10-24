import os
import time
import datetime

'''
c:\\users\\user\\onedrive\\Desktop\\
/Users/name/Desktop/
'''
print(os.path.exists('/Users/pjangala/Desktop/01-09-2025'))

print(os.path.isdir('/Users/pjangala/Desktop/01-09-2025'))
print(os.path.isfile('/Users/pjangala/Desktop/01-09-2025'))

print(os.path.dirname('/Users/pjangala/Desktop/01-09-2025/Day20_OS_file_time_csv/file.py'))
print(os.path.basename('/Users/pjangala/Desktop/01-09-2025/Day20_OS_file_time_csv/file.py'))

print(time.time())
print(time.ctime(time.time()))
t=os.path.getctime('/Users/pjangala/Desktop/01-09-2025/Day20_OS_file_time_csv/file.py')


print(os.name)


os.chdir('/Users/pjangala/Desktop')
print(os.getcwd())

# os.mkdir('TEST')

# os.chdir('/Users/pjangala/Desktop/TEST')

# f=open('test.txt','w')
# f.write('''
# HI hello
#         how are you?
# ''')

# f.close()

# with open('test.txt','r') as re:
#     print(re.read())

# os.remove('test.txt')

# os.makedirs('Grandparent/parent/child')

# os.removedirs('Grandparent/parent/child')

# os.mkdir('TEST')
# os.rename('TEST','DEMO')


