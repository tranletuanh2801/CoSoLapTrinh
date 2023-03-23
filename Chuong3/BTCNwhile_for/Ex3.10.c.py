n=int(input("n="))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i:
            print(j,end="")
    j=j+1
    print()
i=i+1
print()