f=open("input.txt","r")
n=f.readline()
n=int(n)  #chuyen chuoi sang so

st=f.readline()
f.close()
L=st.split()
dem=0
for x in L:
    x=int(x)  #chuyen sang so nguyen
    if x%2==0:
        dem+=1
f=open("output.txt","w")
f.write(str(dem))
f.close()
