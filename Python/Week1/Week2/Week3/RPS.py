# Build a RPS Game
# 2-players
# Each player picks between rock, paper, or scissors
# Each players choice is compared:
# Rock > Scissors
# Scissors > Paper
# Paper > Rock

# 0. Prompt players for their names
# 1. Prompt player 1 for RPS
# 2. Prompt player 2 for RPS
# 3. Compare p1 and p2 shoices to decide a winner

# FIXES
# 1. Check for valid responses
# 2. Hide player inout
# 3. Ste

def RPS():
    
    # Gather player names
    print("Welcome to the Rock, Papaer, Scissors!")
    player1 = input("Player 1, Please enter your name: ")
    player2 = input("Player 2, Please enter your name: ")

    # Gather Player moves
    p1_Choice = input(f"{player1}, choose betweeen Rock, Paper, or Scissors: ")
    while not IsValidMove(p1_Choice):
        print("Invalid Move! Please try again")
        p1_Choice = input(f"{player1}, choose between Rock, Paper, or Scissors: ")

    p2_Choice = input(f"{player2}, choose between Rock, Paper, or Scissors: ")
   
    while not IsValidMove(p2_Choice):
        print("Invalid Move! Please try again")
        p2_Choice = input(f"{player2}, choose between Rock, Paper or Scissors: ")

    # Compare Player Moves
    if p1_Choice == p2_Choice:
        print("It's a draw!")
    
    elif p1_Choice == "rock" and p2_Choice == "scissors":
        print(f"Rock beats scissors, {player1} wins!")
    
    elif p1_Choice == "paper" and p2_Choice == "Rock":
        print(f"Paper beats Rock, {player1} wins!")
    
    elif p1_Choice == "Scissors" and p2_Choice == "Paper":
        print(f"Scissors beats Paper, {player1} wins!")
    
    elif p2_Choice == "rock" and p1_Choice == "scissors":
        print(f"Rock beats scissors, {player2} wins!")

    elif p2_Choice == "paper" and p1_Choice == "Rock":
        print(f"Paper beats Rock, {player2} wins!")

    elif p2_Choice == "Scissors" and p1_Choice == "Paper":
        print(f"Scissors beats Paper, {player2} wins!")

def IsValidMove(playerMove):
    validMoves = ["rock", "paper", "scissors"]

    if playerMove.lower() in validMoves:
        return True
    else:
        return False
    
RPS()