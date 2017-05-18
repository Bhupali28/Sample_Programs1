#!/usr/bin/python



def horiztl_line():
	print (" ---" *board_size)


def vertcl_line():
	print ("|   " *(board_size+1))


board_size = int (input("Enter the size of the board :"))

for i in range (board_size):
	horiztl_line()
	vertcl_line()
	
horiztl_line()
