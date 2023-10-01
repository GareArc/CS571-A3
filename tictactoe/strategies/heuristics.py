
from tictactoe.strategies.advanced_heuristic import advanced_heuristic
from tictactoe.strategies.trail_heuristic import evaluate_heuristic1
from tictactoe.strategies.default_heuristic import evaluate_default    

EVAL_FN_MAP = {
    'default': evaluate_default,
    'heu1': evaluate_heuristic1,
    'adv': advanced_heuristic
}