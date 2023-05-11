n=int(input("n="))


f=open("vd1.txt","w")
# "w" --> mo file, neu file khong ton tai --> tao file moi, neu co thi ghi de
#Ghi so nguyen n vao file
f.write(str(n)+"\n")


#Nhap n so nguyen
st=""
for i in range(n):
    x=input()
    st=st + x + " "
   
f.write(st)
f.close()
