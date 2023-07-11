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

game_images=[rock,paper,scissors]
game_text=["rock","paper","scissors"]

user_choice=int(input("Enter 1 for rock, 2 for paper and 3 for scissor!\n"))
if user_choice>3 or user_choice<=0:
    print("invalid input, you Loose!")
else:
    computer_choice=random.randint(0,2) 
    print("you choose "+game_text[user_choice-1])
    print(game_images[user_choice-1])
    print("Computer choose "+game_text[computer_choice])
    print(game_images[computer_choice])
    if user_choice==computer_choice+1:
        print("its draw!")
    elif user_choice==1 and computer_choice+1==3:
        print("You Win!")
    elif user_choice==3 and computer_choice+1==1:
        print("You loose!")
    elif user_choice-1>computer_choice:
        print("You Win!")
    elif computer_choice>user_choice-1:
        print("You loose!")




