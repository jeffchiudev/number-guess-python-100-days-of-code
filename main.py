import random
from art import logo

#1: pick a random number, save as a global constant e.g. MYSTERY_NUMBER = ?
#2: pick difficulty level, assign variable to determine number of guesses
#3: while loop to continue game until guess is made OR out of guesses e.g. game_over = False
#4: determine if guess is too high aor too low and respond

def game():
  print(logo)
  MYSTERY_NUMBER = random.choice(range(1,101))
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100. Can you guess?")
  print(f"psst, the correct answer is {MYSTERY_NUMBER}")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

game()