n=int(input("n="))
if n==0:
    print(n=0)
else:
    s=1
    for i in range(1,101):
        s=s*i
        print(n,"!=",s,end="")
print()