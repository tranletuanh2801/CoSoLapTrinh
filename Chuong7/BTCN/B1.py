str=input()
dem1=0
dem2=0
dem3=0
dem4=0
for i in str:
    if i.isupper():
        dem1+=1
    elif i.islower():
        dem2+=1
    elif i.isnumeric():
        dem3+=1
    else:
        dem4+=1
print("In hoa:",dem1)
print("In thuong:",dem2)
print("Chu so:",dem3)
print("Khac:",dem4)        