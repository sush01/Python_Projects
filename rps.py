import random

option = ["rock","paper","scissors"]
oponent = random.choice(option)

print("Welcome to Rock Paper Scissor Game!\n")
print("Enter 1 for Rock \nEnter 2 for Paper \nEnter 3 for Scissor\n")

your_choice = int(input("Enter your choice:\n"))

if your_choice not in [1, 2, 3]:
    print("Invalid choice. Please enter a number between 1 and 3.")
else:
    print(f"\nYour choice: {option[your_choice - 1]}, computer's choice: {oponent}")
    

#print(f"\nYou choosed {your_choice}, computer chosed {oponent}")

if your_choice == option.index(oponent)+1:
    print(f"Both players chose {your_choice}. It's a tie!")
elif your_choice == 1:
    if oponent == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif your_choice == 2:
    if oponent == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif your_choice == 3:
    if oponent == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")