from morefunc import *

class Game:
    def __init__(self):
        self._game_state = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self._players = ['X', 'O']

    """"
        This function put the player choice on the board
        :param num of cell that had chosen, the player
    """
    def _move(self, state, num, player):
        i = int((num - 1) / 3)
        j = int((num - 1) % 3)
        state[i][j] = self._players[player]

    """"
        This function print the board in the console
    """
    def _print_board(self):
        print(' ___ . ___ . ___')
        print('|  ' + str(self._game_state[0][0]) + ' |  ' + str(self._game_state[0][1]) + '  |  ' + str
            (self._game_state[0][2]) + ' |')
        print(' ___ . ___ . ___')
        print('|  ' + str(self._game_state[1][0]) + ' |  ' + str(self._game_state[1][1]) + '  |  ' + str
            (self._game_state[1][2]) + ' |')
        print(' ___ . ___ . ___')
        print('|  ' + str(self._game_state[2][0]) + ' |  ' + str(self._game_state[2][1]) + '  |  ' + str
            (self._game_state[2][2]) + ' |')
        print(' ___ . ___ . ___')

    """"
        This function get choice from user 
        :param player_name and player_choice - the cell on the board
    """
    def _play_one_move(self,player_name, player_num):
        print(player_name + "'s turn, choose your cell [1-9]: ")
        player_choice = -1
        while True:
            try:
                player_choice=int(input())
            except ValueError:
                print("this is not a number, please enter a number between 1-9:")
                continue
            else:
                if 1 <= player_choice <= 9:
                    if not is_blocked(self._game_state, player_choice):
                        break
                    else:
                        print("this is block,choose other")
                else:
                    print("please enter a number between 1-9:")

        self._move(self._game_state, player_choice, player_num)
        self._print_board()
        status = check_win(self._game_state)
        return status


