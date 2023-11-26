# Rock Paper Scissor
def rock_paper_scissor(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif player1 == "rock":
        if player2 == "paper":
            return "Player 2 won!"
        else:
            return "Player 1 won!"  
    elif player1 == "paper":
        if player2 == "scissors":
            return "Player 2 won!"
        else:
            return "Player 1 won!"

    elif player1 == "scissors":
        if player2 == "rock":
            return "Player 2 won!"
        else:
            return "Player 1 won!"
    else:
        return "Invalid input, enter correct value."
      
# Driver code
if __name__ == "__main__":
    player1 = input("Enter player 1's choice: ")
    player2 = input("Enter player 2's choice: ")
    print(rock_paper_scissor(player1, player2))  