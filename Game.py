from Board import Board
from Player import Player
import sys
import random

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 0
        self.marker = "X"
        self.player = Player()


    def start_game(self):
        self.help()
        self.board.print_board()
        self.player.get_marker()
        self.board.is_winner(self.marker)

        print("Your marker is " + self.player.player_marker)

        # randomly decide who can play first
        if random.randint(0, 1) == 0:
            print("I will go first")
            self.enter_game_loop('b')
        else:
            print("You will go first")
            self.enter_game_loop('h')

    def end_game(self):
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == 'y':
            self.__init__()  # necessary for re-initialization of the board etc
            self.start_game()
        else:
            print("\n\t-- GAME OVER!!!--\n\t")
            self.quit_game()

    def enter_game_loop(self, turn):
        "starts the main game loop"
        is_running = True
        player = turn  # h for human, b for bot
        while is_running:
            if player == 'h':
                user_input = self.board.get_player_move()
                self.board.make_move(user_input, self.player.player_marker)
                if self.board.is_winner(self.player.player_marker):
                    self.board.print_board()
                    print("\n\tCONGRATULATIONS %s, YOU HAVE WON THE GAME!!! \\tn" % self.player.player_name)
                    # self.incr_score(self.player_name)
                    is_running = False
                    # break
                else:
                    if self.board.is_board_full():
                        self.board.print_board()
                        print("\n\t-- Match Draw --\t\n")
                        is_running = False
                        # break
                    else:
                        self.board.print_board()
                        player = 'b'
            # bot's turn to play
            else:
                bot_move = self.board.get_bot_move(self.player.bot_marker)
                self.board.make_move(bot_move, self.player.bot_marker)
                if self.board.is_winner(self.player.bot_marker):
                    self.board.print_board()
                    print("\n\t%s HAS WON!!!!\t\n" % self.player.bot_name)
                    # self.incr_score(self.bot_name)
                    is_running = False
                    break
                else:
                    if self.board.is_board_full():
                        self.board.print_board()
                        print("\n\t -- Match Draw -- \n\t")
                        is_running = False
                        break
                    else:
                        self.board.print_board()
                        player = 'h'

        # when you break out of the loop, end the game
        self.end_game()

    # def enter_game_loop2(self, turn, user_input):
    #     "starts the main game loop"
    #     is_running = True
    #     player = 'h'  # h for human, b for bot
    #     while is_running:
    #         if player == 'h':
    #             # user_input = self.board.get_player_move()
    #             user_input = int(user_input)
    #             self.board.make_move(user_input, self.player.player_marker)
    #             if self.board.is_winner(self.player.player_marker):
    #                 self.board.print_board()
    #                 return "\n\tCONGRATULATIONS %s, YOU HAVE WON THE GAME!!! \\tn"
    #                 # % self.player.player_name)
    #                 # self.incr_score(self.player_name)
    #                 is_running = False
    #                 # break
    #             else:
    #                 if self.board.is_board_full():
    #                    return board.print_board()
    #                     # print("\n\t-- Match Draw --\t\n")
    #                     is_running = False
    #                     # break
    #                 else:
    #                     return board.print_board()
    #                     player = 'b'
    #         # bot's turn to play
    #         else:
    #             bot_move = self.board.get_bot_move(self.player.bot_marker)
    #             self.board.make_move(bot_move, self.player.bot_marker)
    #             if self.board.is_winner(self.player.bot_marker):
    #                 self.board.print_board()
    #                 return "\n\t%s HAS WON!!!!\t\n"
    #                 # self.incr_score(self.bot_name)
    #                 is_running = False
    #                 break
    #             else:
    #                 if self.board.is_board_full():
    #                     self.board.print_board()
    #                     return "\n\t -- Match Draw -- \n\t"
    #                     is_running = False
    #                     break
    #                 else:
    #                     self.board.print_board()
    #                     player = 'h'
    #
    #     # when you break out of the loop, end the game
    #     self.end_game()

    def human_move(self, user_input):
        user_input = int(user_input)
        self.board.make_move(user_input, self.player.player_marker)

    def bot_move(self):
        bot_move = self.board.get_bot_move(self.player.bot_marker)
        self.board.make_move(bot_move, self.player.bot_marker)

    def quit_game(self):
        "exits game"
        self.board.print_board()
        print("\n\t Thanks for playing :-) \n\t Come play again soon!\n")
        sys.exit()

    def help(self):
        return "\n\t The game board has 9 sqaures(3X3). \n\t Two players take turns in marking the spots/grids on the board. \n\t The first player to have 3 pieces in a horizontal, vertical or diagonal row wins the game. \n\t To place your mark in the desired square, simply type the number corresponding with the square on the grid \n\t Press q to quit \n"




