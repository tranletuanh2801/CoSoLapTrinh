str=input()
str.split()
a=str.split()
a[0]=a[0].capitalize()
for i in range(1,len(a)):
    a[i]=a[i].lower()
new_str=' '.join(a)
new_str=new_str.replace(" ,",",").replace(" ;",";").replace(" :",":").replace(" .",".")
print(new_str)


