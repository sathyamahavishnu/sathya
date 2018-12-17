def largest(arr,n):  
   max=arr[0]  
   for i in range(1, n): 
       if arr[i]>max: 
           max=arr[i] 
   return max 
arr=[1,2,3,4,5] 
n=len(arr) 
lar=largest(arr,n) 
print(lar)
