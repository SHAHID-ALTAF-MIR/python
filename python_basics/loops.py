#for loops

for number in range(1,5):
    print(number,"yahya",number *".")


#for else loop

   
successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
    
else:
    print("sorry failed 3 times")


# nested loops

for x in range (5):
    for y in range(3):
        print(f"({x}, {y})")


#iterable

print(type(5))
print(type(range(5)))               #-----> iterable

for x in "shahid":                  # string are also iterable 
    print(x)

for x in [1,2,3,4,5,6,7,8,9]:       # similarly lists are also iterable 
    print(x)


# while loops

num=100
while num>0:
   
    print(num)
    num//=2


# example of interactive shell in python

#command=""
#while command.lower() != "quit":
 #   command = input(">")
  #  print("echo", command)




#infinite loops

while True:
    command = input(">")
    print("echo" , command)
    if command.lower() == "quit":
        break
