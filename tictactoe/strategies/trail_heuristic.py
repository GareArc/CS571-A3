from tictactoe.objects.types import State


def evaluate_heuristic1(board: State, goal_len: int, board_size: int, **kwargs) -> float:
    """Evaluate the given board based on piece 'x'. The heuristic value is determined by the max_num of 'x' in a row / goal_length.

    Args:
        board (State): _description_
        goal_len (int): _description_
        board_size (int): _description_

    Returns:
        int: _description_
    """
    max_occ = 0.0
    # rows
    for row in range(board_size):
        x_in_row = 0.0
        x_potential = 0.0
        
        x_in_row_max = 0.0
        x_potential_max = 0.0
        for col in range(board_size):
            if board[row][col] == 'x':
                x_in_row += 1
                x_potential += 1
            elif board[row][col] == '':
                x_potential += 1
            else:
                if x_in_row > x_in_row_max:
                    x_in_row_max = x_in_row
                if x_potential > x_potential_max:
                    x_potential_max = x_potential
                x_in_row = 0
                x_potential = 0
        if x_in_row > x_in_row_max:
            x_in_row_max = x_in_row
        if x_potential > x_potential_max:
            x_potential_max = x_potential
            
        if x_potential_max >= goal_len:
            score = (x_in_row_max / goal_len) * 100
            if score > max_occ:
                max_occ = score
    # columns
    for col in range(board_size):
        x_in_col = 0.0
        x_potential = 0.0
        
        x_in_col_max = 0.0
        x_potential_max = 0.0
        for row in range(board_size):
            if board[row][col] == 'x':
                x_in_col += 1
                x_potential += 1
            elif board[row][col] == '':
                x_potential += 1
            else:
                if x_in_col > x_in_col_max:
                    x_in_col_max = x_in_col
                if x_potential > x_potential_max:
                    x_potential_max = x_potential
                x_in_col = 0
                x_potential = 0
        if x_in_col > x_in_col_max:
            x_in_col_max = x_in_col
        if x_potential > x_potential_max:
            x_potential_max = x_potential
            
        if x_potential_max >= goal_len:
            score = (x_in_col_max / goal_len) * 100
            if score > max_occ:
                max_occ = score
                
    # diagonals
                
    for row in range(board_size-1, -1, -1):
        col = 0
        
        x_in_diag = 0.0
        x_potential = 0.0
        x_in_diag_max = 0.0
        x_potential_max = 0.0
        for i in range(min(board_size - row, board_size - col)):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row + i][col + i] == 'x':
                x_in_diag += 1
                x_potential += 1
            elif board[row + i][col + i] == '':
                x_potential += 1

            else:
                if x_in_diag > x_in_diag_max:
                    x_in_diag_max = x_in_diag
                if x_potential > x_potential_max:
                    x_potential_max = x_potential
                x_in_diag = 0
                x_potential = 0
        if x_in_diag > x_in_diag_max:
            x_in_diag_max = x_in_diag
        if x_potential > x_potential_max:
            x_potential_max = x_potential
        if x_potential_max >= goal_len:
            score = (x_in_diag_max / goal_len) * 100
            if score > max_occ:
                max_occ = score
    for row in range(1, board_size):
        row = 0
        
        x_in_diag = 0.0
        x_potential = 0.0
        x_in_diag_max = 0.0
        x_potential_max = 0.0
        for i in range(min(board_size - row, board_size - col)):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row + i][col + i] == 'x':
                x_in_diag += 1
                x_potential += 1
            elif board[row + i][col + i] == '':
                x_potential += 1

            else:
                if x_in_diag > x_in_diag_max:
                    x_in_diag_max = x_in_diag
                if x_potential > x_potential_max:
                    x_potential_max = x_potential
                x_in_diag = 0
                x_potential = 0
        if x_in_diag > x_in_diag_max:
            x_in_diag_max = x_in_diag
        if x_potential > x_potential_max:
            x_potential_max = x_potential
        if x_potential_max >= goal_len:
            score = (x_in_diag_max / goal_len) * 100
            if score > max_occ:
                max_occ = score
    ## (top-right to bottom-left)
    for col in range(board_size):
        row = 0
        
        x_in_diag = 0.0
        x_potential = 0.0
        x_in_diag_max = 0.0
        x_potential_max = 0.0
        for i in range(min(board_size - row, board_size - col)):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row - i][col - i] == 'x':
                x_in_diag += 1
                x_potential += 1
            elif board[row - i][col - i] == '':
                x_potential += 1
            else:
                if x_in_diag > x_in_diag_max:
                    x_in_diag_max = x_in_diag
                if x_potential > x_potential_max:
                    x_potential_max = x_potential
                x_in_diag = 0
                x_potential = 0
        if x_in_diag > x_in_diag_max:
            x_in_diag_max = x_in_diag
        if x_potential > x_potential_max:
            x_potential_max = x_potential
        if x_potential_max >= goal_len:
            score = (x_in_diag_max / goal_len) * 100
            if score > max_occ:
                max_occ = score
                
    for row in range(board_size):
        col = board_size - 1
        
        x_in_diag = 0.0
        x_potential = 0.0
        x_in_diag_max = 0.0
        x_potential_max = 0.0
        for i in range(min(board_size - row, board_size - col)):
            # check if there is a consecutive k pieces for 'x' or 'o'
            if board[row - i][col - i] == 'x':
                x_in_diag += 1
                x_potential += 1
            elif board[row - i][col - i] == '':
                x_potential += 1
            else:
                if x_in_diag > x_in_diag_max:
                    x_in_diag_max = x_in_diag
                if x_potential > x_potential_max:
                    x_potential_max = x_potential
                x_in_diag = 0
                x_potential = 0
        if x_in_diag > x_in_diag_max:
            x_in_diag_max = x_in_diag
        if x_potential > x_potential_max:
            x_potential_max = x_potential
        if x_potential_max >= goal_len:
            score = (x_in_diag_max / goal_len) * 100
            if score > max_occ:
                max_occ = score
            
    return max_occ
