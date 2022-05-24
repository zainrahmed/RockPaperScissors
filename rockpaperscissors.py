#simple Rock, Paper, Scissors Game

print("Rock Paper Scissors")

quit = "play"

rock = {"Rock": "tie", "Paper": "lose", "Scissors": "win"}
paper = {"Rock": "win", "Paper": "tie", "Scissors": "lose"}
scissors = {"Rock": "lose", "Paper": "win", "Scissors": "tie"}
logic = {"Rock": rock, "Paper": paper, "Scissors": scissors}

while(quit != 'quit'):
    player1 = input("Player 1: Type Rock, Paper, or Scissors\n")
    player2 = input("Player 2: Type Rock, Paper, or Scissors\n")
    if logic[player1][player2] == "tie":
        quit = input("Tie game, type 'quit' to quit, enter to continue\n")
    elif logic[player1][player2] == "win":
        quit = input("Player 1 wins, type 'quit' to quit\n")
    else: quit = input("Player 2 wins, type 'quit' to quit\n")


