import re
str=input()
if len(str)<6 or len(str)>17:
    print(False)
else:
    if not re.search('[a-z]',str):
        print(False)
    elif not re.search('[0-9]',str):
        print(False)
    elif not re.search('[A-Z]',str):
        print(False) 
    elif not re.search('[$#@]',str):
        print(False)
    else:
        print(True)
        
        
