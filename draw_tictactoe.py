#!/usr/bin/python

# Tic Tac Toe Draw

def draw_board(game):
   	print ('    |     |   ')
    	print (' ' +str(game[0][0])+ '  |  ' +str(game[0][1])+ '  |   ' +str(game[0][2]) )
    	print ('    |     |   ')
    	print ('---------------')
    	print ('    |     |   ')
    	print (' ' +str(game[1][0])+ '  |  ' +str(game[1][1])+ '  |   ' +str(game[1][2]) )
    	print ('    |     |   ')
    	print('---------------')
	print ('    |     |   ')
    	print (' ' +str(game[2][0])+ '  |  ' +str(game[2][1])+ '  |   ' +str(game[2][2]) )
	print ('    |     |   ')



#def chk_board (game):
def chk_row (game):
	for i in range (0,3):
		row = set([game[i][0] , game[i][1] , game[i][2]])
		#print len(row)
		if game[i][0] != 0 and len(row)== 1 :
			if (game[i][0] == 1) :
				print ("Player 1 won the game in row %d " %(i+1))	
			elif (game[i][0] == 2) :
				print ("Player 2 won the game in row %d " %(i+1))
	return 1
		
def chk_column (game):
	for j in range (0,3):
		col = set([game[0][j] , game[1][j] , game[2][j]])
		if len(col) == 1 and game[0][j] != 0 :
			if (game[0][j] == 1) :
				print ("Player 1 won the game in column %d " %(j+1))	
			elif (game[0][j] == 2) :
				print ("Player 2 won the game in column %d " %(j+1))
	return 2

def chk_diagonally (game):
	if game[1][1] != 0 :
		if (game[0][0] == game[1][1] == game[2][2] == 1) or (game[0][2] == game[1][1] == game[2][0] == 1) :
			print ("Player 1 won the game in diagonally")
		elif (game[0][0] == game[1][1] == game[2][2] == 2) or (game[0][2] == game[1][1] == game[2][0] == 2) :		
			print ("Player 2 won the game in diagonally")

	return 3


def valid_row_col(values):
    	if len(values) != 2:
       		print "Player must enter two values as  row and column "
        	return False
   
    	elif (1 <= int(values[0]) <= 3) and (1 <= int(values[1]) <= 3):
           
           	if game[int(values[0])-1][int(values[1])-1] != 0:
               		print "This place already taken on board."
			print "Play Again"
                	return False
        return True;

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
row_col = []
counter = 0

while True:
	if counter != 9 :
		player = input("Which player wants to play : " + " if player 1 press 1 and if player 2 then press 2 ")
		row_col = input ("In which row and column you want to mark : ")	#Ex : row,col = 0,1
		valid_row_col(row_col)
		while True:
			game[int(row_col[0])-1][int(row_col[1])-1] = player
			counter += 1
			print draw_board(game)
			
			break
	else:
		print ("Game is Over... ")
		break

chk_row (game)
chk_column (game)
chk_diagonally (game)
	
	
	
		
	
	
