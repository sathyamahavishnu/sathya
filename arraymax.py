def largest(arr,n):  
    max=arr[0]  
    for i in range(1, n): 
        if arr[i]>max: 
            ma=arr[i] 
    return max 
arr=[23,56,325] 
n=len(arr) 
lar=largest(arr,n) 
print(lar)
