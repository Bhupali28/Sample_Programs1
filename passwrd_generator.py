#!/usr/bin/python
import random

rand_num = '0123456789'
rand_Lalpha = 'abcdefghijklmnopqrstuvwxyz'
rand_Ualpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rand_symbl = '!@#$%^&*'


passwrd = (str(rand_num)) + rand_Lalpha + rand_Ualpha + rand_symbl

n = input("How many characters do you want in your password : ")
passwrd=''.join(random.sample(passwrd,n))

print passwrd


