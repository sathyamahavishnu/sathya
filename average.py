num = int(input("How many numbers:"))
total_sum = 0
for n in range(num):
    numbers = float(input("numbers:"))
    total_sum += numbers
avg = total_sum/num
print(avg)
