# TIC-TAC-TOE-minimax
in this TIC-TAC-TOE  game there are two modes to play:
Single Player (Against Computer- An implementation of Minimax AI Algorithm)
2 Players.

![Capture](https://user-images.githubusercontent.com/60346583/227796732-73b9a871-08f0-4f26-92a2-09f6919490e3.PNG)

The 2 players mode iteratively takes input from both the players, while making sure, if them input are legale and if anyone has won or not. 

The single player mode uses MiniMax algorithm to make the computer unbeatable. Even if the player plays the most optimal move everytime, the end result would be atmost a draw. Every time you make a move, the computer plays automatically.

![Capture2](https://user-images.githubusercontent.com/60346583/227796819-580d498c-3c34-446c-8fc1-2bc4df78a63d.PNG)

### MiniMax Algorithm
In this algorithm, two players play the game;  The goal of players is to minimize the opponent’s benefit and maximize self-benefit. The MiniMax algorithm conducts a depth-first search to explore the complete game tree and then proceeds down to the leaf node of the tree, then backtracks the tree using recursive calls.
