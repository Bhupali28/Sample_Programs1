#!/usr/bin/python

#import requests
#url = 'https://www.nytimes.com/'
#r = requests.get(url)
#print r.text



import requests
from bs4 import BeautifulSoup
 

r = requests.get('http://www.nytimes.com')
soup = BeautifulSoup(r.text,"html.parser")
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
	print(story_heading.contents[0].strip())
