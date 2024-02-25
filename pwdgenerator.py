import string
import random 

#user enters the length of the password they want to create
len_pwd =int(input("Enter password length:"))

#Display options for character sets
print(""" Choose character sets for password you want to generate
      1. Digits
      2. Letters
      3. Special Characters
      4. Exit """)

#empty string to store the selected character sets 
character_list = ""

while True:
  choice = int(input("Enter number to choose character set:\n"))

  if (choice == 1):
    character_list += string.ascii_letters
  elif (choice ==2):
    character_list += string.digits
  elif (choice == 3):
    character_list += string.punctuation
  elif(choice == 4):
    break
  else: 
    print("Please enter valid option")

#generate password using radomly selected character sets
password = []
for i in range(len_pwd):
  random_character = random.choice(character_list)
  password.append(random_character)

#display the generated password
print("The password is ","".join(password))  
