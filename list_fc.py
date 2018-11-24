thislist = ["fran", "grace", "sasa", "albe"]
print (thislist)
print (thislist[2], "+", thislist[3], "=Perfect")

for x in thislist:
    print (x)


print (len(thislist))


inPerson = input('Search name in the list : ')
if inPerson in thislist:
	print ("YES. It is in the list of ", thislist)
else:
    print ("NO. It is NOT in the list of ", thislist)


conti = 1
while conti == 1:
     addPerson = input ("Enter a new name to the list : ")
     thislist.append(addPerson)
     strConti = input('Add another item (0=STOP or 1=Add more) : ')
     conti = int (strConti)

print (thislist)
