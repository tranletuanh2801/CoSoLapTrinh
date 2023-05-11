str=input()
dem_tu=0
dem_so=0
for i in str:
    if i.isalpha():
        dem_tu+=1
    elif i.isnumeric():
        dem_so+=1
print("chu cai:",dem_tu)
print("chu so:",dem_so)