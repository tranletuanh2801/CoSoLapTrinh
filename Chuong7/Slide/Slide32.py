def checkstring(st1,st2,st3): 
    if st1.startswith(st2) or st1.endswith(st3):
        return True
    return False
st1=input("st1=")
st2=input("st2=")
st3=input("st3=")
kq=checkstring(st1,st2,st3)
print(kq)        