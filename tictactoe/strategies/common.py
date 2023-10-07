from typing import List, Optional, Tuple
from tictactoe.objects.types import EndingType, Move, State


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

def check_end_state(board: State, board_size, goal_len) -> Tuple[bool, Optional[EndingType]]:
        """Check if the game is finished and return the ending type if yes
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
                else:
                    has_sparse = True
                    x_len = 0
                    o_len = 0

                if x_len == goal_len:
                    return True, EndingType.XWIN
                elif o_len == goal_len:
                    return True, EndingType.OWIN
                
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
                else:
                    x_len = 0
                    o_len = 0

                if x_len == goal_len:
                    return True, EndingType.XWIN
                elif o_len == goal_len:
                    return True, EndingType.OWIN
                
        # check if there are goal_len consecutive pieces in the diagonals
        ## (top-left to bottom-right)
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
                else:
                    x_len = 0
                    o_len = 0

                if x_len == goal_len:
                    return True, EndingType.XWIN
                elif o_len == goal_len:
                    return True, EndingType.OWIN
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
                else:
                    x_len = 0
                    o_len = 0

                if x_len == goal_len:
                    return True, EndingType.XWIN
                elif o_len == goal_len:
                    return True, EndingType.OWIN
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
                else:
                    x_len = 0
                    o_len = 0

                if x_len == goal_len:
                    return True, EndingType.XWIN
                elif o_len == goal_len:
                    return True, EndingType.OWIN
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
                else:
                    x_len = 0
                    o_len = 0

                if x_len == goal_len:
                    return True, EndingType.XWIN
                elif o_len == goal_len:
                    return True, EndingType.OWIN


        # check if there are no more moves
        if not has_sparse:
            return True, EndingType.DRAW
        else:
            return False, None