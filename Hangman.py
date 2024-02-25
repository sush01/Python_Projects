import random

wordList = """ monkey bear panda
leopard elephant tiger zebra 
lion wolf  baboon"""

wordList = wordList.split(' ')

word_to_guess = random.choice(wordList)


letter_guessed =''
guessed_word = ['_']*len(word_to_guess)
chances = 7


print("\nWelcome to the word guessing game!")
print(f"Hint:word is a name of wild animal.It is {len(word_to_guess)} letter word" )

while chances > 0 and '_' in guessed_word:
  #print the current word to be guessed 
    print(" ".join(guessed_word))
    guess = input("\nEnter a Letter:").lower()
    
    #check if the guessed letter is in the word
    if guess in word_to_guess:
      print("Correct guess")
      for i in range(len(word_to_guess)):
        if word_to_guess[i]== guess:
          guessed_word[i]= guess
          
    else:
          print("Wrong guess")
          chances -= 1
          
# check if the player guess it all correct          
if '_' not in guessed_word:
   print("Congratulations! You guess all correct.")
else:
  print("You´ve run out of chances. The word was",word_to_guess)        
    