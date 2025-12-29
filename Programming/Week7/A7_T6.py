import random
print()
print("THE ROCK, PAPER, SCISSOR GAME!")
print()
#PLAYER INPUT

player = input("Whats your choice? \nrock, paper or scissor?: ")


#RANDOM COMP. CHOICE
number = random.randint(1, 3)

if number == 1:
    computer = "rock"
elif number == 2:
    computer = "paper"
else:
    computer = "scissors"

print("Computer chose:", computer)

#DECIDE THE WINNER
if player == computer:
    print("It's a tie.")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("Computer wins.")
