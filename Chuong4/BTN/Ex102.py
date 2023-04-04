def nhap():
    so_luong = float(input("Nhap so luong muong ca phe: "))
    return so_luong
def quy_doi():
    
    # if don_vi=="c":  
    #     coc= so_luong
    # elif don_vi == "mc":  
    #     coc = so_luong/16
    # elif don_vi == "tcp":  
    #     coc = so_luong/48
    # else:
    #     return "Đơn vị không hợp lệ."
    so_coc = int(so_coc)
    so_mc = int((so_coc - so_mc)*16)
    so_tcp = round(((so_coc- so_mc - so_tcp / 16) * 48),1)
    
    kq = ""
    if so_coc > 0:
        kq+= str(so_coc) + " cốc"
    if so_mc > 0:
        if kq != "":
            kq+= ", "
        kq += str(so_mc) + " muỗng canh"
    if so_tcp > 0:
        if kq != "":
            kq += ", "
        kq += str(so_tcp) + " thìa cà phê"
    
    return kq
kq=nhap()
quy_doi()

