str=input("str=")
ch=input("ch=")
dem=0
for i in str:
    if i.lower()==ch.lower():
        dem=dem+1
print("Number of character",ch,"is:",dem)