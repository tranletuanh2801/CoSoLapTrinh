# i=9
# while i>=1:
#     print("$"*i)
#     i=i-1
# C2
# i=1
# while i<=9:
#     #in lên màn hình (10-i) dấu $
#     j=1
#     while j<=(10-i):
#         print("$",end="")
#         j=j+1
#     print()
#     i=i+1
#c3
# n=int(input("n="))
# i=n
# while i>=1:
#     print("$"*i)
#     i=i-1   #i-=1
#c4
n=int(input("n="))
i=1
while i<=n:
    # In len man hinh (n+1-i) dau $
    j=1
    while j<= (n+1-i):
        print("$",end="")
        j+=1
    print() #Xuong dong
    i+=1

    
