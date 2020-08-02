


## pseudo code

board with 9 places
each place begins as an empty string   
there are 2 players

player1 chooses a place 
if place is empty string
place is replaced with and X

player2 chooses a place
if place is empty string, 
place is replaced with an O

win_check! (horizontal, diagonal, vertical X's or O's)




board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
mark_choice = input("Player 1 choose mark! 'X' or 'O': ")
x_player = "even"


while mark_choice.lower() not 'x' or mark_choice.lower() not 'o':
    mark_choice = input("Player 1 choose mark! Must be 'X' or 'O': ")
if mark_choice.lower() == 'x':
    x_player == "odd"

def print_board(board):
    print(board)



while not win_check():
    player()


