num = int(input("enter the number"))

n1 = 0
n2= 1
n3 = 0
count = 0
a = []

while(count < num):
	
	a.append(n1)
	n3 = n2 + n1
	n1 = n2
	n2 = n3
	count += 1

print a
