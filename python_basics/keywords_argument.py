#keyword argument  (here by=1 is keyword argument)
def increment(num,by):
    return num+by
print(increment(3,by=1))


#default argument
def increment(number,by=1):    #here we made the by=1 default argument 
    return number+by
print(increment(6))


 #args, wait,what?
def multiply(*numbers):
   total=1
   for number in numbers:
      total*=numbers
    return total

print(1,2,3,4)
