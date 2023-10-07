from typing import List
from tictactoe.objects.types import Move, State


def get_avaliable_moves(board: State, board_size: int) -> List[Move]:
    result = []
    # find empty cells in board
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == '':
                result.append((row, col))
    return result

def move2str(piece: str, move: Move) -> str:
    # move format player — x or o — followed by a number 1, 2, 3, ... for the row, letter a, b, c, ... for the column
    row_str = str(move[0] + 1)
    col_str = chr(ord('a') + move[1])
    
    return f"{piece}{row_str}{col_str}"

def str2move(piece: str, move_str: str) -> Move:
    if move_str[0] != piece:
        raise ValueError(f"Move string {move_str} does not start with {piece}.")
    
    row = int(move_str[1]) - 1
    col = ord(move_str[2]) - ord('a')
    
    return (row, col)