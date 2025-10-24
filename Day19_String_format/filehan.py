# f=open('test1.txt','w')
# f.write('HI, hello world')
# f.writelines('''
# this is my first file handleing
#              i want to create some 
#              text file
# ''')
# f.close()


# file=open('test1.txt','r')
# fi=file.read()
# file.close()


im=open('python.jpeg','rb')

photo=im.read()

im.close()

cim=open('python1.jpeg','wb')

cim.write(photo)

cim.close()




