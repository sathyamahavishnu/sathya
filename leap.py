year = int(input(""))
if(year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
elif(year % 100 == 0):
    print("no")
elif(year % 400 ==0):
    print("Leap Year")
else:
    print("no")
