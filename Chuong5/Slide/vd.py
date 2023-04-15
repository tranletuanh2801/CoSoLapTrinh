# num=[x for x in range(1,6)]
# print(num)

# matrix = [ [x,x-1,x,x-1] for x in range(1,2) ]*3
# matrix=[[1,0,1,0]for x in range(1,4)]
# print(matrix)

# spam=[1,2,3,4,5,6]
# print(spam[-1:3])

#slide24
# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')

#slide30
# catNames=[]
# while True:
#     print("Enter the nam of cat"+ str(len(catNames)+1)+"(Or enter nothing to stop.):") 
#     name=input() 
#     if name=="":
#         break
#     catNames=catNames+[name]
# print("The cat names are:")
# for name in catNames:
#     print(''+name)
    
#slide33
# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# namePet="Pooka"
# if namePet in myPets:
#     print("Index is", myPets.index(namePet))
# else:
#     print("Not Found!")

#slide35
# names = [1, 2, 3, 4, 5, 6]
# names.append(6)
# print(names)
# names.insert(0,7)
# print(names)
# names.insert(-1,8)
# print(names)

numbers = [1, 2, 3, 4, 5]
print(numbers)
del(numbers[0:])
print(numbers)