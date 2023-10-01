from tictactoe.objects.types import State

def _score_consecutive(line, goal_len: int, board_size: int, piece: str) -> float:

    """
    Score a line of the board for a given piece.
    """
    p_len = 0.0
    p_potential = 0.0
    p_len_max = 0.0
    p_potential_max = 0.0
    empty_count = 0
    for i in range(board_size):
        if line[i] == piece:
            p_len += 1
            p_potential += 1
        elif line[i] == '':
            p_potential += 1
            empty_count += 1
        else:
            p_len_max = max(p_len_max, p_len)
            p_potential_max = max(p_potential_max, p_potential)
            p_len = 0
            p_potential = 0
    p_len_max = max(p_len_max, p_len)
    p_potential_max = max(p_potential_max, p_potential)
    # print(f"p_len_max: {p_len_max}, p_potential_max: {p_potential_max}, empty_count: {empty_count}")
    if p_potential_max < goal_len:
        return -100
    
    return ((p_potential_max / goal_len) * 50) + (p_len_max * 30) + empty_count

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
        score_x = max(score_x, _score_row(board, row, goal_len, board_size, 'x'))
        score_o = max(score_o, _score_row(board, row, goal_len, board_size, 'o'))
    print(f"After row: score_x: {score_x}, score_o: {score_o}")
    for col in range(board_size):
        score_x = max(score_x, _score_column(board, col, goal_len, board_size, 'x'))
        score_o = max(score_o, _score_column(board, col, goal_len, board_size, 'o'))
    print(f"After col: score_x: {score_x}, score_o: {score_o}")
    score_x = max(score_x, _score_diagonal(board, goal_len, board_size, 'x'))
    score_o = max(score_o, _score_diagonal(board, goal_len, board_size, 'o'))
    print(f"After diag: score_x: {score_x}, score_o: {score_o}")
    
    return score_x - score_o
    
    
if __name__ == '__main__':
    state = [['x', '', '', ''],
             ['', 'x', '', ''],
             ['', '', 'x', ''],
             ['', '', '', '']]
    print(advanced_heuristic(state, 3, 4))