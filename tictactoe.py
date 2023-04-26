"""
Tic Tac Toe Player
"""
import copy
import math
import numpy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    counter_X = 0
    counter_O = 0
    for row in range(len(board)):
        for i in range(len(board[0])):
            if board[row][i] == X:
                counter_X += 1
            if board[row][i] == O:
                counter_O += 1
    
    if counter_X == counter_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    
    for row in range(len(board)):
        for coloumn in range(len(board[0])):
            if board[row][coloumn] == EMPTY: 
                actions_set.add((row, coloumn))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if action not in actions(board):
        raise ValueError("Invalid Action")

    new_board = copy.deepcopy(board)
    
    if player(board) == X:
        new_board[action[0]][action[1]] = X
    else:
        new_board[action[0]][action[1]] = O
        
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Win condition: 3 in a coloumn
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j]):
            return board[0][j]

    #Win conition: 3 in a row
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
 
    if (board[0][0] == board[1][1] == board [2][2]):
        return board[0][0]
    
    if (board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    else:  
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if winner returns value, then game ends
    if winner(board) != None:
       return True
    
    #Here, after premise above, we funnel down to playing. If there are empty cells, game is not over.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                return False 
    #Finally, the final funnel. If there are no winners and no empty spaces, game ends. 
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    x = winner(board)
    
    if x == 'X':
        return 1
    elif x == 'O':
        return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_action = None

    if player(board) == X:
        v = -10000
        for action in actions(board):
            x = v
            v = max(v, MinValue(result(board, action)))
            if x != v:
                optimal_action = action
                x = v
                    
    else:
        v = 10000
        for action in actions(board):
            x = v
            v = min(v, MaxValue(result(board, action)))
            if x != v:
                optimal_action = action
                x = v
    
    return optimal_action
        
def MaxValue(board):
    
    if terminal(board):
        return utility(board)
    v = -10000
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v
        
def MinValue(board):

    if terminal(board):
        return utility(board)
    v = 10000
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v
    
