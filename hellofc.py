# comment for Python
# https://www.w3schools.com/python/python_strings.asp
# Date: 5/26/2018
print "my first phthon on osx "
text2 = 2*'I am very sorry       ' + '!'
print (text2)

s = str(3.4)     # s will be "3.4"
x = int (2.8)    # x will be 2
y = int ("43")   # y will be 43
z = float ("5")  # z will be 5.0

b = "123456789"
print(b[3:6])    # 456
print(b[0:6])    # 123456

c = "Tom goes to school. Tom breaks his leg."
c = c.replace("Tom", "Mary")
c = c.replace("his", "her")
print (  c)
print (c.split(" "))
cArray = c.split(" ")
print (cArray[0])
print (cArray[4])

d = "I want to have a Fitbit"
print ( d[17:23].lower())
print ( d[17:23].upper())


e = "Albe wants a Fitbit"
print (len( e[13:19]))


x=10
y=20
print('x=',x, ' y=', y, ' \nx*y=', x*y)

numOfTime = input('Num Of time : ')
numInt = int (numOfTime)
iTotal = 0
iBefore = 0
for x in range(1, (numInt + 1)):
    iBefore = iTotal
    iTotal = iTotal + x
    print (iBefore, ' + ', x, ' = ', iTotal)
print ("Total sum = ", iTotal)
print ""
