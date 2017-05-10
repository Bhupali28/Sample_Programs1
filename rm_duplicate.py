#List remove duplicate



def rm_byfun(list1):
	list2 = []
	for i in list1:
		if (i in list2): continue
		else:
			list2.append(i)
	print ("removed duplicate elements by function")	
	print list2

def rm_byset(list1):
	list1 = set(list1)
	list1 = list(list1)
	print ("removed duplicate elements by set")
	print list1



list1 = [0,1,1,2,3,8,5,5,10,27,34]
print ("Original list")
print list1
rm_byfun(list1)
rm_byset(list1) 
#print list1
