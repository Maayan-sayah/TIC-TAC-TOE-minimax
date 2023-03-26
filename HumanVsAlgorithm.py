import random
from math import inf as infinity
import time
import Game as game
from morefunc import *


class HumanVsAlgorithm(game.Game):
    pass

    """"
    this recursive function execute the minmax algorithm 
    that choose the better move for the computer
    :param state of board, which player do the move
    :return a score for the every move 
    """
    def __choose_best_move(self, state, player):
        if player == 1:
            best = [-1, -infinity]
        else:
            best = [-1, +infinity]

        status = check_win(state)
        empty_cells = find_empty_cells(state)
        if status == "X":  # the player won
            return [-1, -1 * len(empty_cells)]
        elif status == "O":  # the computer won
            return [-1, 1 * len(empty_cells)]
        elif status == "end":
            return [-1, 0]

        for cell in empty_cells:
            new_state = copy(state)
            self._move(new_state, cell, player)
            if player == 1:
                move = self.__choose_best_move(new_state, 0)
            else:
                move = self.__choose_best_move(new_state, 1)

            if player == 1:
                if move[1] > best[1]:
                    best[0] = cell  # max value
                    best[1] = move[1]
            else:
                if move[1] < best[1]:
                    best[0] = cell  # min value
                    best[1] = move[1]

        return best

    """"
     Tossing up a coin to choose the start player
     and start the first rotate
    """
    def __first_rotate(self, player_name):
        # Tossing up a coin to choose the start player
        random_num = random.randint(0, 2)
        # the first rotate
        if random_num == 0: # human start
            print(player_name + ", you will start")
            self._play_one_move(player_name, 0)
            time.sleep(1)
            print("computer turn:")
            time.sleep(1)
        else: # computer start
            print("the computer will start")
        choice = random.randint(0, 9)
        while is_blocked(self._game_state, choice):
            choice=random.randint(0, 9)
        self._move(self._game_state, choice, 1)
        self._print_board()
        time.sleep(1)

    """"
    the main function of the game
    """
    def start(self):
        # open the game, get name from user
        player_name = input("player- enter your name:")
        while player_name == "":
            player_name = input("no name, enter again ")
        print(player_name + " we start to play ! ")
        self._print_board()

        # first rotate
        self.__first_rotate(player_name)

        # The main loop of the game
        status = ""
        while status == "":
            status = self._play_one_move(player_name, 0)
            if status != "":
                break
            time.sleep(1)
            print("the computer turn:")
            comp_choise = self.__choose_best_move(self._game_state, 1)  # minmax algorithm
            self._move(self._game_state,comp_choise[0],1)
            self._print_board()
            status = check_win(self._game_state)
            time.sleep(1)

        return ret_scores(status,player_name,"computer")


