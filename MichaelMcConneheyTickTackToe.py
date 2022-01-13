'''
Tick Tack Toe Game
Michael McConnehey
'''

def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    player1 = 'x'
    player2 = 'o'
    board = create_board()
    display_board(board)
    # loop if there isn't a winner or if the game isn't a draw
        # display the board

        # allow the player to make a move

        # pick the next player

    # display the final board

    # show message for winner and thanks for playing
    pass

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = []
    for i in range(9):
        i += 1
        board.append(i)
    
    return board

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    print(f'\n{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    
    return

def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    pass

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    pass

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    pass      

def next_player(current):
    ''' return: x if current is o, otherwise x '''
    pass

# run main if this has been called from the command line
if __name__ == "__main__":
    main()