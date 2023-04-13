import re
def check_password_strength(password):
    if len(password) < 8:
        return "False"         
    if not re.search('[A-Z]', password):
        return "False"    
    if not re.search('[a-z]', password):
        return "False"       
    if not re.search('[0-9]', password):
        return "False"     
    return "True"
password = input("Hay nhap mat khau cua ban: ")
print(check_password_strength(password))