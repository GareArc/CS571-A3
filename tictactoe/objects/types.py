from typing import List, Tuple
from enum import Enum

Move = Tuple[int, int]
State = List[List[str]]

class EndingType(Enum):
    """Enum for the ending type of a game."""
    XWIN = 0
    OWIN = 1
    DRAW = 2