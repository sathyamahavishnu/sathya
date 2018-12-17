no=int(input(""))
temp=no
sum=0
while no>0:
    rem=no%10
    sum=sum+rem*rem*rem
    no=no//10
if sum==temp:
    print("amstrong number")
else:
    print(" not amstrong number")
