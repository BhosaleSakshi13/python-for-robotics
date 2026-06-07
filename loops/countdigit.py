num = int(input("Enter multiple digit number :"))
count = 0

while num != 0:
	num //= 10
	count += 1

print(count)

