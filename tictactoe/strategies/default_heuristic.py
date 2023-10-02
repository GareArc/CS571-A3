from tictactoe.objects.types import State


def evaluate_default(board: State, goal_len: int, board_size: int, **kwargs) -> int:
    """Evaluate the given board based on piece 'x'. No heuristic involved.
    
    Args:
        board (State): The board to evaluate
    
    Returns:
        int: The evaluation of the given board
    """
    # check rows
    for row in range(board_size):
        x_len = 0
        o_len = 0
        for col in range(board_size):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row][col] == 'x':
                x_len += 1
                o_len = 0
            elif board[row][col] == 'o':
                o_len += 1
                x_len = 0

            if x_len >= goal_len - 1:
                return 1
            elif o_len >= goal_len - 1:
                return -1
            
    # check columns
    for col in range(board_size):
        x_len = 0
        o_len = 0
        for row in range(board_size):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row][col] == 'x':
                x_len += 1
                o_len = 0
            elif board[row][col] == 'o':
                o_len += 1
                x_len = 0

            if x_len >= goal_len - 1:
                return 1
            elif o_len >= goal_len - 1:
                return -1
            
    # check diagonals
    for row in range(board_size-1, -1, -1):
        col = 0
        x_len = 0
        o_len = 0
        for i in range(min(board_size - row, board_size - col)):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row + i][col + i] == 'x':
                x_len += 1
                o_len = 0
            elif board[row + i][col + i] == 'o':
                o_len += 1
                x_len = 0

            if x_len >= goal_len - 1:
                return 1
            elif o_len >= goal_len - 1:
                return -1
    for col in range(1, board_size):
        row = 0
        x_len = 0
        o_len = 0
        for i in range(min(board_size - row, board_size - col)):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row + i][col + i] == 'x':
                x_len += 1
                o_len = 0
            elif board[row + i][col + i] == 'o':
                o_len += 1
                x_len = 0

            if x_len >= goal_len - 1:
                return 1
            elif o_len >= goal_len - 1:
                return -1
    ## (top-right to bottom-left)
    for col in range(board_size):
        row = 0
        x_len = 0
        o_len = 0
        for i in range(col+1):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row + i][col - i] == 'x':
                x_len += 1
                o_len = 0
            elif board[row + i][col - i] == 'o':
                o_len += 1
                x_len = 0

            if x_len >= goal_len - 1:
                return 1
            elif o_len >= goal_len - 1:
                return -1
    for row in range(1, board_size):
        col = board_size - 1
        x_len = 0
        o_len = 0
        for i in range(board_size - row):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row + i][col - i] == 'x':
                x_len += 1
                o_len = 0
            elif board[row + i][col - i] == 'o':
                o_len += 1
                x_len = 0

            if x_len >= goal_len - 1:
                return 1
            elif o_len >= goal_len - 1:
                return -1

    return 0