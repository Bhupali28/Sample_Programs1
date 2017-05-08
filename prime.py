n = input ("enter the number ")
a = []

for i in range (1,n+1):
	if n%i == 0:
		a.append(i)
if len(a)==2:
	print("number is prime")
else:
	print ("number is not prime")

print 'and factors are = ' , str(a)
