from HumanVsAlgorithm import HumanVsAlgorithm
from HumanVsHuman import HumanVsHuman
import time
from morefunc import *

menu_str = "~~~~~~~~~~~~~~~~~~~~\n" \
          "choose option:\n" \
          "1) 2 players game \n" \
          "2) 1 players game \n" \
          "3) scores table\n" \
           "enter q to quit\n" \
          "~~~~~~~~~~~~~~~~~~~~\n"

def main():
    scores_table = {}
    print("TIC TAC TOE GAME!!!")
    inp = input(menu_str)
    while(1):
        inp.replace(" ","")
        if inp == "1":
            game_instance = HumanVsHuman()
            scores = game_instance.start()
            add_score_to_table(scores, scores_table)
        elif inp == "2":
            game_instance = HumanVsAlgorithm()
            scores = game_instance.start()
            add_score_to_table(scores, scores_table)
        elif inp == "3":
            print_score_table(scores_table)
        elif inp == "q":
            print("thank you! bye")
            break;
        else:
            print("input error, enter again")
            inp = input()
            continue

        time.sleep(1)
        inp = input(menu_str)
        inp.replace(" ", "")

if __name__ == "__main__":
    main()