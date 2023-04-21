while True:
    password=input()
    if len(password)>=8 and password.isalnum():
        print("Hợp lệ")
        break
    
    print("Không hợp lệ")

