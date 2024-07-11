import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_pics = [rock, paper, scissors]
your_choice = int(input("Choose you weapon? 0 for Rock, 1 for Scissors, and 2 for Paper \n"))
print("You chose:")
if your_choice >= 3 or your_choice < 0:
    print("Invalid number you lose")
else:
    print(game_pics[your_choice])
    cpu_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_pics[cpu_choice])
    if your_choice == 0 and cpu_choice == 2:
        print("Winner Winner Chicken Dinner!")
    elif cpu_choice == 0 and your_choice == 2:
        print("You lose!!")
    elif cpu_choice > your_choice:
        print("You lose!")
    elif your_choice > cpu_choice:
        print("Winner Winner chicken dinner!!")
    elif cpu_choice == your_choice:
        print("Draw!!")
    elif your_choice >= 3 or your_choice < 0:
        print("Invalid number you lose")
