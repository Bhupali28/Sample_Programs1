import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

f = open("birthday.json", "r")
Birthdays = json.load(f)

output_file("plot.html")

listMonth = []
month_list = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

for date in Birthdays :
	month = Birthdays[date].split("/")
	month=int(month[0])
	listMonth.append(month_list[month])
	
#Counter(listMonth)
x_categories = month_list.values()

p = figure(x_range=x_categories)


p.vbar(x=Counter(listMonth).keys(), top=Counter(listMonth).values(), width=0.5)


show(p)
