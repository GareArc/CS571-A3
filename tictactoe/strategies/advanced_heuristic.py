from numpy import number
from tictactoe.objects.types import State

def _score_candidate(candidates: list[int], goal_len: int) -> float:
    result = None
    # print(f"candidates: {candidates}")
    for p_len, p_potential in candidates:
        if p_len >= goal_len // 2:
            return 200*goal_len
        score = p_len*100 + p_potential*50
        if result is None:
            result = score
        else:
            result = max(result, score)
    # print(f"result: {result}")
    return result
        

def _score_consecutive(line, goal_len: int, board_size: int, piece: str) -> float:

    """
    Score a line of the board for a given piece.
    """
    result = -500.0
    p_len = 0.0
    p_potential = 0.0
    candidates = []
    # print(f"line: {line}")
    empty = 0.0
    for i in range(board_size):
        if line[i] == piece:
            p_len += 1
            p_potential += 1
            if p_len >= goal_len:
                return 1000*goal_len
            # print(f"item:{line[i]}, p_len: {p_len}, p_potential: {p_potential}, empty: {empty}")
        elif line[i] == '':
            p_potential += 1
            empty += 1
            # print(f"item:{line[i]}, p_len: {p_len}, p_potential: {p_potential}, empty: {empty}")
        else:
            if p_potential >= goal_len:
                candidates.append((p_len, p_potential))
            p_len = 0.0
            p_potential = 0.0
            # print(f"item:{line[i]}, p_len: {p_len}, p_potential: {p_potential}, empty: {empty}")
    if p_potential >= goal_len:
                candidates.append((p_len, p_potential))
            
    can_score = _score_candidate(candidates, goal_len)
    if can_score is not None:
        result = can_score
    return result

def _score_column(board: State, col: int, goal_len: int, board_size: int, piece: str) -> float:
    """
    Score a column of the board for a given piece.
    """
    column = [board[i][col] for i in range(board_size)]
    return _score_consecutive(column, goal_len, board_size, piece)

def _score_row(board: State, row: int, goal_len: int, board_size: int, piece: str) -> float:
    """
    Score a row of the board for a given piece.
    """
    return _score_consecutive(board[row], goal_len, board_size, piece)

def _score_diagonal(board: State, goal_len: int, board_size: int, piece: str) -> float:
    """
    Score a diagonal of the board for a given piece.
    """
    score = 0.0
    # top-right to bottom-left
    for row in range(board_size):
        col = 0
        line = [board[row + i][col + i] for i in range(min(board_size - row, board_size - col))]
        score = max(score, _score_consecutive(line, goal_len, min(board_size - row, board_size - col), piece))
        # print(f"line: {line}, score: {_score_consecutive(line, goal_len, min(board_size - row, board_size - col), piece)}")
    for col in range(1, board_size):
        row = 0
        line = [board[row + i][col + i] for i in range(min(board_size - row, board_size - col))]
        score = max(score, _score_consecutive(line, goal_len, min(board_size - row, board_size - col), piece))
        # print(f"line: {line}, score: {_score_consecutive(line, goal_len, min(board_size - row, board_size - col), piece)}")
    # top-left to bottom-right
    for col in range(board_size):
        row = 0
        line = [board[row + i][col - i] for i in range(col+1)]
        score = max(score, _score_consecutive(line, goal_len, col+1, piece))
        # print(f"line: {line}, score: {_score_consecutive(line, goal_len, col+1, piece)}")
    for row in range(1, board_size):
        col = board_size - 1
        line = [board[row + i][col - i] for i in range(board_size - row)]
        score = max(score, _score_consecutive(line, goal_len, board_size - row, piece))
        # print(f"line: {line}, score: {_score_consecutive(line, goal_len, board_size - row, piece)}")
    return score
            

def advanced_heuristic(board: State, goal_len: int, board_size: int, **kwargs) -> float:
    """
    Advanced heuristic function for tic-tac-toe(x).
    """
    score_x = 0.0
    score_o = 0.0
    for row in range(board_size):
        row_x = _score_row(board, row, goal_len, board_size, 'x')
        row_o = _score_row(board, row, goal_len, board_size, 'o')

        score_x = max(score_x, row_x)
        score_o = max(score_o, row_o)
    # print(f"After row: score_x: {score_x}")
    for col in range(board_size):
        col_x = _score_column(board, col, goal_len, board_size, 'x')
        col_o = _score_column(board, col, goal_len, board_size, 'o')

        score_x = max(score_x, col_x)
        score_o = max(score_o, col_o)
    # print(f"After col: score_x: {score_x}")
    diag_o = _score_diagonal(board, goal_len, board_size, 'o')
    diag_x = _score_diagonal(board, goal_len, board_size, 'x')

    score_o = max(score_o, diag_o)
    score_x = max(score_x, diag_x)
    # print(f"After diag: score_x: {score_x}")
    return score_x - score_o
    
    
if __name__ == '__main__':
    state = [['x', 'o', ''],
             ['', 'x', ''],
             ['', '', 'o']]
    print(advanced_heuristic(state, 3, 3))
    
    # print(_score_consecutive(['x','o','','','','','','','',''], 4, 10, 'x'))