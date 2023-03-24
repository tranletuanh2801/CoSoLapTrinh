
# n=int(input("n="))
# m=n
# i=0
# while n>=1:
#     i=i+1
#     n//=10
# print(m, "co ",i ,"chu so")

#c4
n=int(input("n="))
so=n
if n!=0:
    dem=0
    while n>0:
        n=n//10 #n=int(n/10)
        dem=dem+1
else :
    dem=1
print(so,"co",dem,"chu so")