#!/usr/bin/python
# Reverse word order

word = raw_input("enter the word :")
#str_split1 = []

str_split = list(word.split())
rev_list = str_split[::-1]


rev_list=' '.join(rev_list)

print 'Final output :',rev_list

