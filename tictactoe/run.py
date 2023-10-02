import argparse
from tictactoe.objects.T3Game import T3Game

def get_args():
    parser = argparse.ArgumentParser(description="Start a tic-tac-toe game!")
    parser.add_argument('board_size', type=int, help='Board size of the game')
    parser.add_argument('goal_length', type=int, help='How many in a row to win')
    parser.add_argument('play_order', type=str, help='x/o, x if you goes first, o if AI goes first')
    parser.add_argument('--agents', type=str, default='ah', help='Types of agents: aa, ah, hh')
    parser.add_argument('--depth', type=int, default=8, help='Depth of minimax search')
    parser.add_argument('--eval', type=str, default='default', help='default/heu1')
    parser.add_argument('--print', type=bool, default=True, help='Print out the board after each move')
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    print(f"Starting a tic-tac-toe game with board size {args.board_size}, goal length {args.goal_length}")
    
    game = T3Game(args)
    
    game.run_game()
