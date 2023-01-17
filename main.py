import random


listOfWords = ["hilarious", "protect", "foreigner", "colon", "get", "decade", "rain", "shell", "crutch", "essential"]

myWord = random.choice(listOfWords)
lives = len(myWord) # is a function that returns the number of items in an object
letterPicked = [] #this is empty list called "letterPicked" to keep track of all the letters the user has picked.

print("🌟Hangman🌟")
print()

while True:
  userChoice = input("choose a letter: ").lower() #method so that the code can compare it to the letters in the word regardless of the case.
  if userChoice in letterPicked:
    print("You have picked that before, try again..")
    continue #to loop back at start
    
  letterPicked.append(userChoice)
  
  if userChoice in myWord:
    print("You found a letter!")
    
  else:
    print("nope, not in there")
    lives -= 1

  allLeters = True #At the beginning of the loop, before the user has picked any letters, the code sets allLeters to True. Then, as the user picks letters, the code loops through the letters of the word and checks if each letter has been picked by the user. If a letter has not been picked yet, the code sets allLeters to False and continues to the next letter. 
#After the loop, if allLeters is still True, it means that the user has picked all the letters in the word and the user wins the game. If allLeters is False, it means that the user has not picked all the letters yet and the game continues.
  print()
  for i in myWord:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLeters = False
      
  print( )
  
  if lives == 0:
    print(f"first time huh? the answer is {myWord}")
    break
  if allLeters:
    print(f"you just entered matrix. you win with {lives} left")
    break
  else: 
    print(f"{lives} left")