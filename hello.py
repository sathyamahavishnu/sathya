def new(number,loop):
     if loop == 1:
         return number
     else:
         return number * new(number,loop-1)
a = new(6,6)
print a
print "Hello"*a
