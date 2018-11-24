print ('Let us learn "string" for python')

str="albe babySmartGirl"
print (str)

print (str[0])
print (str[2])
print (str[4])
print (str[6])

print (str[0:4])
print (str[9:14])

str2="   hey!   "
print ('len=',len(str2))

str3 = str2.strip()
print ('len=', len(str3), '  >', str3, '< ')

print(str3.upper())

str5 = "lastname|firstname|phone Num|address|city|state"
print (str5.split("|"))
arry5 = str5.split("|")
print (arry5[2])
print (arry5[4])
