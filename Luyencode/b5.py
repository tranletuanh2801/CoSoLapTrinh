L=[]
T=[]
while True:
    x=int(input())
    if x==0:
        break
    else:
        L.append(x)
for i in L:
    if i>0 and i%2==0:
        T.append(i)
if len(L) == 0:
    print('Khong hop le')
elif len(T)==0:
    print(0)
else:
    print(sum(T)/len(T))



# def inp():
#     n=int(input())
#     return n 
# def FeeShip(n):
#     if n==0:
#         cost=0
#     else:
#         cost=5.95+(n-1)*3.75
#     return cost
# def ShowFee(cost):
#     print(cost)
# n=inp()
# cost=FeeShip(n)
# ShowFee(cost)    


# A = []
# N = []
# M = []
# while True:
#     x=int(input())
#     ifx==0:
#         break
#     else:
#         A.append(x)
# for i in A:
#     if i%2==0:
#         N.append(i)
#     if i%2==1:
#         M.append(i)
# N.sort()
# M.sort()
# for i in N: 
#     print(i,end=' ')
# print()
# for i in M:
#     print(i,end=' ')
    
    
# A = []
# M = []
# N = []

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         A.append(n)

# for i in A:
#     if i % 2 == 0:
#         N.append(i)
#     else:
#         M.append(i)

# N.sort()
# M.sort()

# for i in N:
#     print(i,end=' ')
# print()
# for i in M:
#     print(i, end=' ')