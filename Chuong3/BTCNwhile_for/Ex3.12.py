n=input()
m={"0":"A","1":"B","2":"C","3":"D","4":"E","5":"F","6":"G","7":"H","8":"K","9":"L"}
ketqua=""
for so in n:
    if so in m:
        ketqua+=m[so]
print(ketqua)


