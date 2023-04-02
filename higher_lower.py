import random
from data import data

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

condi = True
score = 0
while condi == True:
    print(logo)
    rando = random.choice(data)
    print(f"Compare A: {rando['name']}, {rando['description']}, {rando['country']}")
    print(vs)
    rando2 = random.choice(data)
    print(f"Compare B: {rando2['name']}, {rando2['description']}, {rando2['country']}")
    guess = input("Who has more follower? Type 'A' or 'B'  ")
    