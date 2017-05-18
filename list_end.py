

	
def new_list(list):
	#return (list[0],list[-1])
	list1 = []
	list1.append(list[0])
	list1.append(list[-1])
	return list1    	

list = ['First',20,1,3,455,'Last']
#list1 = []
list1 = new_list(list)
print list1
