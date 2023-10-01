
from unittest import result
from tictactoe.objects.T3Board import T3Board
from tictactoe.objects.Player import AIAgent, Agent, HumanAgent
from tictactoe.objects.types import EndingType


class T3Game:
    player_o: Agent
    player_x: Agent
    
    def __init__(self, args):
        self.args = args
        
        self.board = T3Board(args.board_size, args.goal_length)
        self._init_players()
        
    def _init_players(self):
        if self.args.agents == 'aa': 
            self.player_x = AIAgent('x', self.args.eval, self.args.depth)
            self.player_o = AIAgent('o', self.args.eval, self.args.depth)
        elif self.args.agents == 'ah':
            if self.args.play_order == 'x':
                self.player_x = HumanAgent('x')
                self.player_o = AIAgent('o', self.args.eval, self.args.depth)
            else:
                self.player_o = HumanAgent('o')
                self.player_x = AIAgent('x', self.args.eval, self.args.depth)
        else:
            self.player_x = HumanAgent('x')
            self.player_o = HumanAgent('o')
            
    def run_game(self):
        game_board = T3Board(self.args.board_size, self.args.goal_length)
        # game_board.test()
        # exit()
        
        while not game_board.check_end()[0]:
            if self.args.print:
                game_board.print_board()
            
            # player x's turn
            print("Player x's turn")
            move = self.player_x.get_next_move(board=game_board)
            game_board.add_piece('x', move[0], move[1])
            
            if game_board.check_end()[0]:
                break
            
            if self.args.print:
             game_board.print_board()
            
            print("Player o's turn")
            # player o's turn
            move = self.player_o.get_next_move(board=game_board)
            game_board.add_piece('o', move[0], move[1])
            
        print("Game finished!")
        game_board.print_board()
        status = game_board.check_end()[1]
        if status == EndingType.XWIN:
            print("Player x wins!")
        elif status == EndingType.OWIN:
            print("Player o wins!")
        else:
            print("It's a draw!")