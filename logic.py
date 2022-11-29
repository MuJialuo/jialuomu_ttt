# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

# updated Nov 29, 2022
# jialuomu@uw.edu

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board, turn):
    x = 0
    y = 0 
    letter_won = None
    
    #check
    while x < 3:
        if board[x][y] == board[x][y+1] == board[x][y+2]:
            if board[x][y] != None:
                letter_won = board[x][y]
        x = x + 1
    x = 0
    while y < 3:
        if board[x][y] == board[x+1][y] == board[x+2][y]:
            if board[x][y] != None:
                letter_won = board[x][y]
        y = y + 1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != None:
            letter_won = board[x][y]
    elif board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != None:
            letter_won = board[x][y]
    
    print('letter_won', letter_won)

    #output
    if letter_won != 'Draw':
        return letter_won
    elif letter_won == 'Draw':
        return None
    elif turn == 8:
        return letter_won


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O"  # FIXME