#jacob cook
#tic-tac-toe
#11/11/2019

#Global Constant
X = "X"
O = "O"
NUM_SQUARES = 9
TIE = "TIE"
EMPTY = " "

#working
def instructions():
     """Welcome to tic-tac-toe."""
     print(
          """
     Welcome to tic-tac-toe
     you will always lose because your up against the computer
     first to 3 in a row wins
     the board is 1-9 choose where to place your x or o

     1 | 2 | 3
     ---------
     4 | 5 | 6
     ---------
     7 | 8 | 9

     the games about to begin. \n
     """
     )

#working
def ask_yes_no(question):
     """Ask yes or no question"""
     response = None
     while response not in ("yes","no","y","n"):
          response = input(question).lower()
     x = response[0]
     return x

#working
def new_board():
     board = []
     for i in range(NUM_SQUARES):
          board.append(EMPTY)
     return board

#working
def display_board(board):
     print(str.format("""
     {0} | {1} | {2}
     ---------
     {3} | {4} | {5}
     ---------
     {6} | {7} | {8}
     """,board[0],board[1],board[2],
                  board[3],board[4],
                  board[5],board[6],
                  board[7],board[8]))


def pieces():
     go_first = ask_yes_no("do you require the first move? y/n: ")
     if go_first == "y":
          print("\ni thought so")
          human = X
          comp = O
     else:
          print("\nYou shoul of taken the first move")
          comp = X
          human = O
     return comp,human

def ask_number(question, low, high):
     response = None
     while response not in range(low, high):
          try:
               response = int(input(question))
          except:
               print("thats not a number")
     return response

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
##
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Whats your move? (1-9):",1,NUM_SQUARES+1)-1
        if move not in legal:
            print("\nThat was a dumb move KID! Choose another.\n")
    print("Fine.......")
    return move
##
#board = new_board()
#move = human_move(board,x)
#print(move)
       
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
##
def winner(board):
     WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
     for row in WAYS_TO_WIN:
          if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
               winner = board[row[0]]
               return winner
     if EMPTY not in board:
         return TIE

     return None
def congrat_winner(winner, comp, human) :
     if winner != TIE:
          print(winner, "won!\n")
     else:
          print("its a tie")
     if winner == comp:
          print("As I predicted, human, I am triumphant once more.  \n" \
              "Proof that computers are superior to humans in all regards.")
     elif winner == human:
          print("No, no!  It cannot be!  Somehow you tricked me, human. \n" \
              "But never again!  I, the computer, so swear it!")
     elif winner == TIE:
          print("You were most lucky, human, and somehow managed to tie me.  \n" \
              "Celebrate today... for this is the best you will ever achieve.")

def comp_move(board, human, comp):
     board_copy = board[:]
     BEST_MOVES = (4,0,2,6,8,1,3,5,7)
     print("i want square number", end=" ")
     for move in legal_moves(board):
          board_copy[move] = comp
          if winner((board_copy)) == comp:
               print(move+1)
               return move
          board_copy[move] = EMPTY

     for move in legal_moves(board):
          board_copy[move] = human
          if winner(board_copy) == human:
               print(move+1)
               return move
          board_copy[move] = EMPTY
     for move in BEST_MOVES:
          if move in legal_moves(board):
               print(move+1)
               return move
     
     
def game():
     instructions()
     comp , human = pieces()
     board = new_board()
     turn = X
     display_board(board)
     win = winner(board)
     while not winner(board):
          if turn == human:
               move = human_move(board,human)
               board[move] = human
               turn = next_turn(turn)
          else:
               move = comp_move(board, human, comp)
               board[move] = comp
               turn = next_turn(turn)
          display_board(board)
          win = winner(board)
          congrat_winner(win, comp, human)
          


game()
