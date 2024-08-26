print("Let's play wordle!\nGuess the Wordle in 6 tries.\nEach guess must be a valid 5-letter word.\nFor each guess, a hint will tell you how many letters you've guessed correctly:\nA G represents a letter in the word and in the correct spot.\nA Y represents a letter in the word but in the wrong spot.\nA _ represents a letter not in the word in any spot.\nGuess below!")

word = "water"

def makeAGuess(guess):
  hint = ""
  for i in range(len(word)):
    if (word[i])== guess[i]:
      hint += "G"

    elif guess[i] in word:
      hint += "Y"

    else: 
      hint += "_"
  print(hint)
  return(hint)

for i in range(5):
  user_guess = input()
  hint = makeAGuess(user_guess)
  if hint != "GGGGG":
    print("you did not solve the puzzle try again")
  elif hint == "GGGGG":
    print("congratulations on solving the puzzle")
    break  

## TASK A: Define a variable 'word' that holds the correct word for the wordle game
## TASK B: Define a function 'makeAGuess()' that passes in a users guess as a parameter
## TASK C: Define a variable 'hint' that holds an empty string
## TASK D: Build a loop that loops from 0 to the length of word
# TASK E: Check if the current letter of guess matches the current letter of word. If so add the letter "G" to the hint
# TASK F: If the previous condition is fales, check if the current letter of guess is in word at all. If so add the letter "Y" to the hint
# TASK G: If the previous two conditions are false, add the symbol "-" to the hint
# TASK H: Return hint

# TASK I: Build a loop that loops 6 times (representing the number of guesses a user has)
  # TASK J: Define a variable 'guess'. prompt the user for their 5-letter guess and store it in the variable
  # TASK K: Define a variable 'hint' and set the return of makeAGuess(guess) to that variable
  # TASK L: Print hint
  # TASK M: Check if hint = "GGGGG". If so the user has won. Print a win message and break the loop
# TASK N: After the loop has finished, meaning the user has run out of guesses, check if hint != "GGGGG". If so, the user has lost. Print a lose message. 