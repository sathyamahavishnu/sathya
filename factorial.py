def factorial(num):
    if num == 1:
       return num
    else:
       return num * factorial(num - 1)
num=int(input(""))
if num<0:
   print("Factorial  negative number")
elif num==0:
   print("Factorial of 0 is 1")
else:
   print(factorial(num))
