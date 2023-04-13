def isInteger(s): 
	s = s.strip()
	if len(s) <= 0: 
		return False
	else:
		if s[0] == '+' or s[0] == '-':
			for i in range (1, len(s), 1):
				if (s[i] > 9 or s[i] < 1):
					return False
		else: 
			for i in range (0, len(s), 1):
				if (s[i] > 9 or s[i] < 1):
					return False
	return True
s = int(input("Nhap so: "))
if isInteger(s):
	print("Chuoi dai dien cho mot so nguyen hop le")
else:
	print("Chuoi khong dai dien cho mot so nguyen hop le")