print ('Python file  2018/11/25 Sunday ')
my_file=open("/Users/fchiang/dev/python/in_test_fc.txt","r")
#Use print to print the line else will remain in buffer and replaced by next statement
for line in my_file:
    print(line)
my_file.close()


fruits=["Orange\n","Banana\n","Apple\n"]
new_file2=open("/Users/fchiang/dev/python/out_test_fc.txt",mode="w+",encoding="utf-8")
new_file2.writelines(fruits)
for line in new_file2:
    print(line)
new_file2.close()
