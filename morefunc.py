""""
    This function test if someone win or the game is over in tie.
    Victory is tested vertically, horizontal and diagonally
    :return "O"/"X" for the winner, "" if the game not over or "end" if the game over in tie
"""
def check_win(state):
    for i in range(0, 3):  # check horizon
        if (state[i][0] == state[i][1] == state[i][2]) and state[i][0] != ' ':
            return state[i][0]
    for i in range(0, 3):  # check vertical
        if (state[0][i] == state[1][i] == state[2][i]) and state[0][i] != ' ':
            return state[0][i]
    if (state[0][0] == state[1][1] == state[2][2]) and state[0][0] != ' ':
        return state[0][0]
    if (state[0][2] == state[1][1] == state[2][0]) and state[0][2] != ' ':
        return state[0][2]

    end_game = 1
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == ' ':
                end_game = 0
                break
    if end_game == 1:
        return "end"

    return ""

""""
this func check if specific cell in board is block
"""
def is_blocked(state, num):
    i = int((num - 1) / 3)
    j = int((num - 1) % 3)
    if state[i][j] != ' ':
        return 1
    else:
        return 0

""""
this func get the user's name in 2 players game 
"""
def get_name_from_user():
    player1_name = input("player1- enter your name:")
    while player1_name == "":
        player1_name = input("no name, enter again ")
    player2_name = input("player2- enter your name:")
    while player2_name == "":
        player2_name = input("no name, enter again ")

    return player1_name,player2_name

""""
this function check if the player exist in table score 
and add his points to his general score
"""
def add_score_to_table(scores,scores_table):
    for score in scores.keys():
        if score in scores_table.keys():
            scores_table[score] += scores[score]
        else:
            scores_table[score] = scores[score]


""""
this function print the score table to the console
"""
def print_score_table(scores_table):
    if len(scores_table)==0:
        print("no scores yet")
    else:
        print("~~~~ score table ~~~~")
        for player in scores_table.keys():
            print(player + ": "+str(scores_table[player]) + " points")
        print("~~~~~~~~~~~~~~~~~~~~~~")

""""
this function iterate  on the board and find the empty cell
"""
def find_empty_cells(state):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                empty_cells.append(i * 3 + (j + 1))
    return empty_cells

"""
this function create a copy of the board
"""
def copy(state):
    new_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(3):
        for j in range(3):
            new_state[i][j] = state[i][j]
    return new_state

""""
this func get the status of the game and return the relative scores
"""
def ret_scores(status,player1_name,player2_name):
    if status == "end":
        print("the game is over,no one win")
        return {player1_name: 1, player2_name: 1}
    elif status == "X":
        print("Congratulations " + player1_name + "! you won!")
        return {player1_name: 2, player2_name: 0}
    else:
        if player2_name=="computer":
            print("sorry, the computer won ")
        else:
            print("Congratulations " + player2_name + "! you won!")
        return {player1_name: 0, player2_name: 2}