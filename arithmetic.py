def sumOfAP( a, d,n): 
   sum=0
   i=0 
   while i<n : 
         sum = sum+a 
         a=a+d 
         i=i+1
   return sum
n=int(input(""))
a=int(input(""))
d=int(input(""))
print(sumOfAP(a, d, n)) 
