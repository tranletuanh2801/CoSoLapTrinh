# n=int(input())
# if n%4==0 :
#     print('Co')
# elif n%100==0 and n%400==0:
#     print('Co')
    
# else:
#     print('Khong')
    
#  n=input().split()
# st=''.join(n)
# kq=int(st)
# print(kq)
   


   
# st=input().split()
# dem=0
# for i in st:
#     if len(i)<=5:
#         dem+=1
# print(dem)  

# str=input()
# a=str.split(', ')
# L=[]
# for i in a:  
#     L.append(i)
# L.sort(reverse=True)
# new=' '.join(L)  
# print(new) 

n=input().split(', ')
n=[int(a) for a in n]
n.sort(reverse=True)
for a in n:
    print(a,end=' ')
# c=' '.join(n)
# print(c)
# n=input().split()
# L=list(n)
# B=list(L)
# max=0
# for i in range(0,len(L)-1,2):
#     if B[i].L[i+1]>max:
#         print(max)
    
#     elif B[i+1].L[i]>max:
#         print(max)
    
# for i in B:
#     print(i,end=" ")

# str=input().split(', ')
# a=[int(a) for a in str]
# L=[]
# for i in a:
    
#     L.append(i)
# L.sort(reverse=True)
# new=' '.join(L)  
# print(new) 