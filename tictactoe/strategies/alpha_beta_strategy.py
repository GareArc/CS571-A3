
from typing import List, Tuple

from tictactoe.objects.types import Move, State
from tictactoe.objects.T3Board import T3Board
from tictactoe.strategies.common import get_avaliable_moves, move2str
from tictactoe.strategies.default_heuristic import evaluate_default

def _minimax(board: State, piece: str, depth: int, is_max_plyr: bool, alpha: float, beta: float, goal_len: int, board_size: int, evaluate_fn) -> int:
    if depth == 0 or len(get_avaliable_moves(board, board_size))==0:
        return evaluate_fn(board, goal_len, board_size)
    
    if is_max_plyr:
        max_eval = float('-inf')
        for move in get_avaliable_moves(board, board_size):
            board[move[0]][move[1]] = 'x'
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
            board[move[0]][move[1]] = 'o'
            eval = _minimax(board, piece, depth - 1 if depth > 0 else depth, True, alpha, beta, goal_len, board_size, evaluate_fn)
            board[move[0]][move[1]] = ''
            
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move_by_ab(board: T3Board, is_x: bool, depth: int = -1, eva_fn = evaluate_default) -> Move:
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
        score = _minimax(board_state, piece, depth, not is_x, alpha, beta, goal_len, board_size, eva_fn)
        board_state[row][col] = '' # undo move
        
        print(f"Move({piece}): {move2str(piece, move)}, score: {score}")
        
        if is_x and (best_score is None or score > best_score):
            best_score = score
            best_move = move
        elif not is_x and (best_score is None or score < best_score):
            best_score = score
            best_move = move
            
    return best_move

if __name__ == '__main__':
    from tictactoe.strategies.advanced_heuristic import advanced_heuristic
    board = T3Board(3, 3)
    board.board = [['x', 'o', 'x'],
             ['x', 'o', ''],
             ['', '', '']]
    board.print_board()
    
    find_best_move_by_ab(board, False, -1, advanced_heuristic)
    
    
    
    