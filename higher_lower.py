import random
from data import data
import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

condi = True
score = 0
while condi == True:
    print(logo)
    rando = random.choice(data)
    print(f"Compare A: {rando['name']}, {rando['description']}, {rando['country']}")
    print(vs)
    rando2 = random.choice(data)
    print(f"Compare B: {rando2['name']}, {rando2['description']}, {rando2['country']}")
    guess = input("Who has more follower? Type 'A' or 'B'  ").lower()

    is_correct = check_answer(guess, rando['follower_count'], rando2['follower_count'])

    clear = lambda: os.system('clear')
    clear()
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      condi = False
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
