num = int(raw_input("enter the number"))

sum = 0
temp = num
while (temp > 0):
	no = temp % 10
	sum += no ** len(str(num))
	temp /= 10
print sum
if (sum == num):
	print ("The number is Armstrong")
else:
	print ("The number is not Armstrong")
