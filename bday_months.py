#!/usr/bin/python

# Birthday months

import json
from collections import Counter

f = open("birthday.json", "r")
Birthdays = json.load(f)
listMonth = []
month_list = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

for date in Birthdays :
	month = Birthdays[date].split("/")
	month=int(month[0])
	listMonth.append(month_list[month])
	#month.append(month_list[month])
	
print Counter(listMonth)

