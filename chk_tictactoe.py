#!/usr/bin/python

# check Tic Tac Toe

#def chk_row (game):
#	for i in range (0,3):
#		if (game[i][0] == game[i][1] == game[i][2] == 1) :
#			print ("Player 1 won the Tic Tac Toe game in row %d " %(i))
#		elif (game[i][0] == game[i][1] == game[i][2] == 2) :
#			print ("Player 2 won the Tic Tac Toe game in row %d " %(i))
		
#def chk_column (game):
#	for j in range (0,3):
#		if (game[0][j] == game[1][j] == game[2][j] == 1) :
#			print ("Player 1 won the Tic Tac Toe game in column %d " %(j))
#		elif (game[0][j] == game[1][j] == game[2][j] == 2) :
#			print ("Player 2 won the Tic Tac Toe game in column %d " %(j))	
	
#def chk_diagonally (game):
#	if (game[0][0] == game[1][1] == game[2][2] == 1) or (game[0][2] == game[1][1] == game[2][0] == 1) :
#		print ("Player 1 won the Tic Tac Toe game in diagonally")
#	elif (game[0][0] == game[1][1] == game[2][2] == 2) or (game[0][2] == game[1][1] == game[2][0] == 2) :		
#		print ("Player 2 won the Tic Tac Toe game")
	 
	



#game = [[2, 1, 1],
#	[2, 2, 0],
#	[2, 1, 1]]
#print game
#chk_row (game)
#chk_column (game)
#chk_diagonally(game)

###############################################################################################################

#!/usr/bin/python

# check Tic Tac Toe


def chk_row (game):
	for i in range (0,3):
		row = set([game[i][0] , game[i][1] , game[i][2]])
		#print len(row)
		if game[i][0] != 0 and len(row)== 1 :
			if (game[i][0] == 1) :
				print ("Player 1 won the game in row %d " %(i))	
			elif (game[i][0] == 2) :
				print ("Player 2 won the game in row %d " %(i))
		
def chk_column (game):
	for j in range (0,3):
		col = set([game[0][j] , game[1][j] , game[2][j]])
		if len(col) == 1 and game[0][j] != 0 :
			if (game[0][j] == 1) :
				print ("Player 1 won the game in column %d " %(j))	
			elif (game[0][j] == 2) :
				print ("Player 2 won the game in column %d " %(j))

def chk_diagonally (game):
	if game[1][1] != 0 :
		if (game[0][0] == game[1][1] == game[2][2] == 1) or (game[0][2] == game[1][1] == game[2][0] == 1) :
			print ("Player 1 won the game in diagonally")
		elif (game[0][0] == game[1][1] == game[2][2] == 2) or (game[0][2] == game[1][1] == game[2][0] == 2) :		
			print ("Player 2 won the game in diagonally")



game = [[0, 1, 1],
	[2, 2, 2],
	[2, 1, 1]]
print game
chk_row (game)
chk_column (game)
chk_diagonally (game)





























