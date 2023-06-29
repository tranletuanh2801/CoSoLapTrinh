def nhap():
    st=input()
    return st
def Xuly(st):
    tach=st.split('Email:')
    email=tach[-1].strip()
    if email==' ':
        print()
    else:
        print(email)
st=nhap()
Xuly(st)