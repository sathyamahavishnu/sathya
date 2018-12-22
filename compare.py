str1 = raw_input("")
str2 = raw_input("")
count1 = 0
count2 = 0
for i in str1:
       count1=count1+1
for j in str2:
       count2=count2+1
if(count1<count2):
       print("")
       print(str2)
elif(count1==count2):
       print("strings are equal")
else:
       print("Larger")
       print(str1)
