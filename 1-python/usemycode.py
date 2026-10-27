import mycode 

print(mycode.person)

mycode.say_hi("Alice")

#never really import function in center of code 
from mycode import say_hi

say_hi("Bob")

import mycode as local_mycode
print(local_mycode.person)