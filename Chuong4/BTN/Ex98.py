def hex2int(chuoihex = 'A79D'):
    tdhex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    gt = 0
    for i in range(len(chuoihex)):
        char = chuoihex[i].upper()
        if char in tdhex:
            gt += tdhex[char] * (16 ** (len(chuoihex) - i - 1))
    return gt
def int2hex(chuoiint = 192330):
    chuoi = ''
    chuyenhex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while chuoiint != 0: 
        n = chuoiint % 16
        if n in chuyenhex:
            chuoi = chuyenhex[n] + chuoi
        else:
            chuoi = str(n) + chuoi
        chuoiint = chuoiint // 16
    return chuoi
print(hex2int())
print(int2hex())

