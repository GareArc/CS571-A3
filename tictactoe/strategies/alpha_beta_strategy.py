
from typing import List, Tuple

from tictactoe.objects.types import Move, State
from tictactoe.objects.T3Board import T3Board
from tictactoe.strategies.common import get_avaliable_moves, move2str

def _evaluate_heuristic1(board: State, goal_len: int, board_size: int, **kwargs) -> int:
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
    for row in range(board_size - goal_len + 1):
        for col in range(board_size - goal_len + 1):
            x_in_diag = 0.0
            x_potential = 0.0
            
            x_in_diag_max = 0.0
            x_potential_max = 0.0
            for i in range(goal_len):
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
    return max_occ

def _evaluate_default(board: State, goal_len: int, board_size: int, **kwargs) -> int:
    """Evaluate the given board based on piece 'x'. No heuristic involved.
    
    Args:
        board (State): The board to evaluate
    
    Returns:
        int: The evaluation of the given board
    """
    has_sparse = False
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

            if x_len == goal_len:
                return 1
            elif o_len == goal_len:
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

            if x_len == goal_len:
                return 1
            elif o_len == goal_len:
                return -1
            
    # check diagonals
    for row in range(board_size - goal_len + 1):
        for col in range(board_size - goal_len + 1):
            x_len = 0
            o_len = 0
            for i in range(goal_len):
                # check if there is a consecutive k pieces for 'x' or 'o'
                if board[row + i][col + i] == 'x':
                    x_len += 1
                    o_len = 0
                elif board[row + i][col + i] == 'o':
                    o_len += 1
                    x_len = 0

                if x_len == goal_len:
                    return 1
                elif o_len == goal_len:
                    return -1

    return 0

def _minimax(board: State, piece: str, depth: int, is_max_plyr: bool, alpha: float, beta: float, goal_len: int, board_size: int, evaluate_fn) -> int:
    eval = evaluate_fn(board, goal_len, board_size)
    if depth == 0 or eval is not None:
        return eval
    
    if is_max_plyr:
        max_eval = float('-inf')
        for move in get_avaliable_moves(board, board_size):
            board[move[0]][move[1]] = piece
            eval = _minimax(board, piece, depth - 1 if depth > 0 else depth, False, alpha, beta, goal_len, board_size, evaluate_fn)
            board[move[0]][move[1]] = ''
            
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_avaliable_moves(board, board_size):
            board[move[0]][move[1]] = piece
            eval = _minimax(board, piece, depth - 1 if depth > 0 else depth, True, alpha, beta, goal_len, board_size, evaluate_fn)
            board[move[0]][move[1]] = ''
            
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move_by_ab(board: T3Board, is_x: bool, depth: int = -1, eva_fn = _evaluate_default) -> Move:
    """Find the best move for the given piece on the given board using alpha-beta pruning
    
    Args:
        board (T3Board): The board to find the best move on
        piece (str): The piece to find the best move for
        is_x (bool): Whether the piece is 'x'
        depth (int): The remaining avaliable depth of the search tree, -1 for no depth limit
    
    Returns:
        Tuple[int, int]: The best move (row, col) for the given piece on the given board
    """
    piece = 'x' if is_x else 'o'
    board_state = board.deep_copy()
    goal_len = board.goal_len
    board_size = board.board_size
    
    best_move = None
    best_score = None
    alpha = float('-inf')
    beta = float('inf')
    
    for move in get_avaliable_moves(board_state, board_size):
        row, col = move
        board_state[row][col] = piece
        score = _minimax(board_state, piece, depth, is_x, alpha, beta, goal_len, board_size, eva_fn)
        board_state[row][col] = '' # undo move
        
        print(f"Move({piece}): {move2str(piece, move)}, score: {score}")
        
        if is_x and (best_score is None or score > best_score):
            best_score = score
            best_move = move
        elif not is_x and (best_score is None or score < best_score):
            best_score = score
            best_move = move
            
    return best_move

EVAL_FN_MAP = {
    'default': _evaluate_default,
    'heu1': _evaluate_heuristic1
}
    
    