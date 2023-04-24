def NhapHoten():
    while True:
        hoten=input('Ho ten: ')
        if hoten.istitle():
            return hoten
        else:
            print("Không hop le!!!")
hoten=NhapHoten()