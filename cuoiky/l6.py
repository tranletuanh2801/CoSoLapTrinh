# chuyển chuỗi thành 1 số nguyên
# n=input().split()
# st=''.join(n)
# kq=int(st)
# print(kq)

# min max trong chuỗi số và chữ
# def Input():
#     st=input()
#     return st
# def Xuly(st):
#     s=[]
#     for i in range(len(st)):
#         if st[i].isnumeric():
#             s.append(st[i])
#     print([int(max(s)),int(min(s))])
# st=Input()
# Xuly(st)


# trùng lặp
# st=input().split()
# L=[]
# for i in st:
#     if i not in L:
#         L.append(i)
# for i in L:
#     print(i,end=' ')

def Input():
    n=int(input())
    L=[]
    for i in range(n):
        a=input()
        L.append(a)
    return n,L
def Output(n,L):
    if n<=0:
        return None
    max=0
    tu=''
    for a in L:
        if len(a)>max:
            max=len(a)
            tu=a
    print(max)
    print(tu)
n,L=Input()
Output(n,L)

        
    
