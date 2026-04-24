#def salam():
 #   print("asalamu")
  #  print("alaikum")


#salam()


#arguments

def salam(first_name,last_name):
    print("asalamu")
    print(f"alaikum {first_name} {last_name}")


salam("yahya","zameer")
salam ("shahid" , "altaf mir")




#types of functions


#1. functions which perform a task
def greet(name):
    print(f"hi{name}")
    greet("shahid")
#2. functions which return a value
def get_greeting(name):
    return f"hi {name}"

msg=get_greeting("mosh")
file = open("content.txt","w")
file.write(msg)


