
def rev_str(string):

	return string[::-1]


string = raw_input("Please enter a string ")

rev_str = rev_str(string)

print(rev_str)

if (string == rev_str):
	print("This string is a palindrome")
else:
	print("This string is not a palindrome")
