#Jeg ser ikke et peong med å kommenterer alt her
print("Hei verden")
print("Hei igjen")

fname = "donald"
lname = "duck"

print(fname + lname)

number1 = "1"
number2 = "1"

print(number1 + number2)

number1 = 1
number2 = 1

print(number1 + number2)


number2 = 2
if number1 > number2:
    print("1 er mindre enn 2")
else:
    print("2 er større enn 1")

i = 1

while i < 5:
    print("loop:" + str(i))
    i += 1

for i in range(6):
    print("loop: " + str(i))

def myfunction():
    print("print fra funksjon")

myfunction() 
    