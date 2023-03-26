import Game as game
from morefunc import *
import time

class HumanVsHuman(game.Game):
    pass

    """"
    the main function of the game
    """
    def start(self):
        player1_name, player2_name = get_name_from_user()
        print(player1_name + ",  " + player2_name + " we start playing ! ")
        self._print_board()

        status = ""
        while status == "":  # The main loop of the game
            status= self._play_one_move(player1_name, 0) # player1 turn
            if status != "":
                break
            time.sleep(1)
            status= self._play_one_move(player2_name, 1) # player2 turn
            time.sleep(1)

        # end of game
        return ret_scores(status, player1_name, player2_name)
