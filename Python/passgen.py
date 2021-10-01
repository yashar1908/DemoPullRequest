import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [1,2,3,4,5,6,7,8,9]
characters = ["!","@","#","$","%","^","&","*","(",")"]
letn = int(input("How many letters do you want?"))
numn = int(input("How many numbers do you want?"))
charn = int(input("How many special characters do you want?"))
password = ""
for i in range (1,letn+1):
    password += (random.choice(letters))
for i in range (1,numn+1):
    password += str(random.choice(numbers))
for i in range (1,charn+1):
    password += random.choice(characters)
strlist = list(password) #converting string to list to use random.shuffle()
random.shuffle(strlist) #using function to shuffle a list in random order
password = ''.join(strlist) #converting the list back to string
#random.shuffle() only be working with lists hence the conversion
print("Password is:",password)
