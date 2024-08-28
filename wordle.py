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

print("Let's play wordle!\nGuess the Wordle in 6 tries.\nEach guess must be a valid 5-letter word.\nFor each guess, a hint will tell you how many letters you've guessed correctly:\nA G represents a letter in the word and in the correct spot.\nA Y represents a letter in the word but in the wrong spot.\nA _ represents a letter not in the word in any spot.\nGuess below!")
for i in range(5):
  user_guess = input()
  hint = makeAGuess(user_guess)
  if hint != "GGGGG":
    print("you did not solve the puzzle try again")
  elif hint == "GGGGG":
    print("congratulations on solving the puzzle")
    break  
