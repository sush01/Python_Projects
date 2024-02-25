import random
import math

"""
number_list = [1,4,7,8,9,4]
answer = random.choice(number_list)

attempts = 5

while attempts > 0:
  guess_number = int(input("Enter your guess:\n"))
  
  if guess_number == answer:
    print(f"Congratulations!You guessed it right. Answer is {answer}")
    break
  else:
    attempts -= 1
    print("Wrong guess!Better luck next time!")
 
if attempts == 0:
    print(f"Sorry! you have no more attempts left. The answer was {answer}")
    """

random_number = random.randint(1,50)    
count = 0

while count < 6:
  count += 1
  your_guess = int(input("Guess any number from 1 to 50:"))
  
  if your_guess == random_number:
    print("Congratulation!You guessed right.")
    break
  elif your_guess > random_number:
    print("You guess too high!")
  elif your_guess < random_number:
    print("You guessed too low!")
else:
  print(f"Sorry you are out of attempts!The answer was {random_number}")