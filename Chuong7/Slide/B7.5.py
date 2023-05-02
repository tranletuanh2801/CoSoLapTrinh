str=input()
dem1=0
dem2=0
for i in str:
    if i.isalpha():
        dem1+=1
    elif i.isnumeric():
        dem2+=1
print("chu cai:",dem1)
print("chu so:",dem2)