# str=input().split(',')
# L=[]
# for i in str:
#     if int(i,2)%3==0:
#         L.append(i)
# if L:
#     print(','.join(L))
# else:
#     print()

# def nhap():
#     str=input().split(',')
#     return str
# def In(str):
#     L=[]
#     for i in str:
#         if int(i,2)%3==0:
#             L.append(i)
#     if L:
#         print(','.join(L))
#     else:
#         print()
# str=nhap()
# In(str)

st=input().split(',')
L=[]
for i in st:
    if int(i,2)%3==0:
        L.append(i)
print(','.join(L))
        
    