    
import time
from typing import Callable, Tuple
from tictactoe.objects.T3Board import T3Board
from tictactoe.objects.types import Move
from tictactoe.strategies.alpha_beta_strategy import find_best_move_by_ab
from tictactoe.strategies.common import move2str, str2move

import os

from tictactoe.strategies.heuristics import EVAL_FN_MAP


class Agent:
    piece = None
    move_file_name = None
    
    def get_next_move(self, **kwargs):
        raise NotImplementedError("This method must be implemented by a subclass.")
    
    
class AIAgent(Agent):
    def __init__(self, piece: str, eval_fn: str, depth) -> None:
        super().__init__()
        self.piece = piece
        self.move_file_name = f"{piece}moves.txt"
        self.eval_fn = EVAL_FN_MAP[eval_fn]
        self.depth = depth
        
    def get_next_move(self, **kwargs):
        """Get the next move by running a provided strategy and record it in file.
        
        """
        board: T3Board = kwargs['board']
        move = find_best_move_by_ab(board, self.piece=='x', self.depth, eva_fn=self.eval_fn)
        
        # append move to file
        with open(self.move_file_name, 'a') as f:
            f.write(move2str(self.piece, move))
            f.flush()
            f.close()
            
        return move
    
class HumanAgent(Agent):
    def __init__(self, piece: str) -> None:
        super().__init__()
        self.piece = piece
        self.move_file_name = f"{piece}moves.txt"
        self.last_mod_time = self._get_mod_time()
    
    def _get_mod_time(self):
        return os.stat(self.move_file_name).st_mtime
        
    def get_next_move(self, **kwargs):
        # wait for change in file
        while self.last_mod_time == self._get_mod_time():
            time.sleep(0.1)
        self.last_mod_time = self._get_mod_time()
        # read last line
        move = None
        with open(self.move_file_name, 'r') as f:
            lines = f.readlines()
            # print(lines)
            last_line = lines[-1].strip()
            move = str2move(self.piece, last_line)
        return move
            
        
    