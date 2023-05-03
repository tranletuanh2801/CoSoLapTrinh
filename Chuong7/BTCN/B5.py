str=input().split(' ')
x=int(input())
index=-1
for i in range(len(str)):
    if int(str[i])==x:
        index=i
        break
if index!=-1:
    print(index+1)
else:
    print(0)
