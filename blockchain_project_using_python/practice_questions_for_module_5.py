# IMPORT THE RANDOM FUNCTION AND GENERATE BOTH A RANDOM NUMBER BETWEEN 0 & 1 AS WELL AS A RANDOM NUMBER BETWEEN 1 & 10. 
import random
import datetime
import hashlib
a=random.random()
print(a)           

b=random.randint(1,10)
print(b)

# USE THE DATETIME LIBRARY TOGETHER WITH THE RANDOM NUMBER TO GENERATE A RANDOM, UNIQUE VALUE.
c=datetime.datetime.now()
x= hashlib.sha256((str(a)+str(c)).encode()).hexdigest()
print(x)