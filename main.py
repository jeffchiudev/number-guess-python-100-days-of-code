import random
from art import logo

#1: pick a random number, save as a global constant e.g. MYSTERY_NUMBER = ?
#2: pick difficulty level, assign variable to determine number of guesses
#3: while loop to continue game until guess is made OR out of guesses e.g. game_over = False
#4: determine if guess is too high aor too low and respond

def game():
  print(logo)

  MYSTERY_NUMBER = random.choice(range(1,101))
  game_over = False
  guesses = 0

  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100. Can you guess?")
  print(f"psst, the correct answer is {MYSTERY_NUMBER}")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if difficulty == "easy":
    guesses += 10
  else:
    guesses += 5

  print(f"You chose {difficulty} and have {guesses} attempts to guess the number.")

  while not game_over:
    player_guess = int(input("Make a guess: "))
    if player_guess == MYSTERY_NUMBER:
      print(f"You got it! The answer was {MYSTERY_NUMBER}")
      game_over = True
    elif guesses == 1:
      if player_guess > MYSTERY_NUMBER:
        print("Too high.")
      elif player_guess < MYSTERY_NUMBER:
        print("Too low.")
      print("Sorry, you're out of guesses. Game over")
      game_over = True
    elif player_guess > MYSTERY_NUMBER:
      print("Too high.")
      print("Guess Again.")
      guesses -= 1
      print(f"You have {guesses} attempts left.")
    elif player_guess < MYSTERY_NUMBER:
      print("Too Low.")
      print("Guess Again.")
      guesses -= 1
      print(f"You have {guesses} attempts left.")
    
    

game()