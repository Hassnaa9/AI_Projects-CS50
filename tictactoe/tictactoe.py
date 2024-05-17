"""
Tic Tac Toe Player
"""

import math

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
    x_count = sum(row.count(X) for row in board)  #count X
    o_count = sum(row.count(O) for row in board)  #count O
    if x_count <= o_count:                        #x must be forward by one
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    p_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                p_actions.add((i, j))
    return p_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i>=0 and i<3 and j<3 and j>=0 :
        if board[i][j] != EMPTY:    # precondition to check the incoming pos is valid or not
            raise NotImplementedError
    if i>=0 and i<3 and j<3 and j>=0 :
        new_board = [row[:] for row in board]   # create new board to update it with the new move
        new_board[i][j] = player(board)
        return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O
    # Check columns
    for j in range(3):
        if all(board[i][j] == X for i in range(3)):
            return X
        elif all(board[i][j] == O for i in range(3)):
            return O
    # Check diagonals
    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        return O

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        value, action = max_value(board)
    else:
        value, action = min_value(board)
    return action

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    optimal_action = None
    for action in actions(board):
        minv, _ = min_value(result(board, action))
        if minv > v:
            v = minv
            optimal_action = action
    return v, optimal_action

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    optimal_action = None
    for action in actions(board):
        maxv, _ = max_value(result(board, action))
        if maxv < v:
            v = maxv
            optimal_action = action
    return v, optimal_action
