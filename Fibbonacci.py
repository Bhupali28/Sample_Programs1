#num = int(input("enter the number"))

def fibo_series(n1,n2,num):
	
	n3 = 0
	count = 0
	a = []

	while(count <= num):
	
		a.append(n1)
		n3 = n2 + n1
		n1 = n2
		n2 = n3
		count += 1

	return a

n1 = int(input("enter the 1st number"))
n2= int(input("enter the 2nd number"))
num = input("How many fibonacci numbers would you like to generate?")
fibo_series = fibo_series(n1,n2,num)
print fibo_series



