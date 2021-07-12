from random import randint
from art import logo

#1: pick a random number, save as a global constant e.g. MYSTERY_NUMBER = ?
#2: pick difficulty level, assign variable to determine number of guesses
#3: while loop to continue game until guess is made OR out of guesses e.g. game_over = False
#4: determine if guess is too high aor too low and respond

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """Compares guess to answer, returns number of turns remaining"""
  if guess > answer: 
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it, the answer was {answer}.")


def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)

  MYSTERY_NUMBER = randint(1, 100)
  # game_over = False

  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100. Can you guess?")
  print(f"psst, the correct answer is {MYSTERY_NUMBER}")
  turns = set_difficulty()
  player_guess = 0
  # difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  # if difficulty == "easy":
  #   guesses += 10
  # else:
  #   guesses += 5


  while player_guess != MYSTERY_NUMBER:
    print(f"You have {turns} attempts to guess the number.")
    player_guess = int(input("Make a guess: "))
    turns = check_answer(player_guess, MYSTERY_NUMBER, turns)
    if turns == 0:
      # if player_guess > MYSTERY_NUMBER:
      #   print("Too high.")
      # elif player_guess < MYSTERY_NUMBER:
      #   print("Too low.")
      print("Sorry, you're out of guesses. Game over")
      return
    elif player_guess != MYSTERY_NUMBER:
      print("Guess Again.")



game()