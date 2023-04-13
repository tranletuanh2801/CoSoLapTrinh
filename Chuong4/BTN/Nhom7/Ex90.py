def isInteger(char):
    char = char.strip() 
    if len(char)<1:
        return False
    else: 
        if char[0] in ['+','-'] and  char[1:].isdigit(): 
            return True
        elif char.isdigit():
            return True
        else:
            return False
char = input('Nhap chuoi:')
if isInteger(char)==True: print('Chuoi la so nguyen!')
else: print('Chuoi khong phai la so nguyen!')
        
 
 
 
