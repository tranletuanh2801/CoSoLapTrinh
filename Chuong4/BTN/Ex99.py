def sang_thap_phan(so,he_so):
    thap_phan = 0
    mu = 0
    chu_so = "0123456789ABCDEF"
    for chu_so_hien_tai in str(so)[::-1]:
        thap_phan += chu_so.index(chu_so_hien_tai) * he_so ** mu
        mu += 1
    return thap_phan
def sang_he_so_moi(thap_phan,he_so_moi):
    ket_qua = ''
    chu_so = "0123456789ABCDEF"
    while thap_phan > 0:
        phan_du = thap_phan % he_so_moi
        ket_qua = chu_so[phan_du] + ket_qua
        thap_phan = thap_phan // he_so_moi
    return ket_qua
def main():
    he_so_ban_dau = int(input("Nhap vao he co so ban dau (2-16): "))
    he_so_moi = int(input("Nhap vao he co so muon chuyen doi (2-16): "))
    so = input("Nhap vao so can chuyen doi: ")
    if he_so_ban_dau < 2 or he_so_moi > 16:
        print("Loii!!! (Chuong trinh chi ho tro he co so tu 2 den 16.) hay nhap laii!!!")
        return
    thap_phan = sang_thap_phan(so, he_so_ban_dau)
    ket_qua = sang_he_so_moi(thap_phan, he_so_moi)
    print(f"Ket qua chuyen doi so {so} tu he co so {he_so_ban_dau} sang he co so {he_so_moi}: {ket_qua}")
if __name__ == '__main__':
    main()
