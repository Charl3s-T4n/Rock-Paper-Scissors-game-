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

#Write your code below this line 👇
user_decision=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#For user's decision
if user_decision == 0:
  print(rock)
elif user_decision == 1:
  print(paper)
elif user_decision == 2:
  print(scissors)


#For computer's decision
print("Computer chose: ")
import random
random_number_chosen=random.randint(0,2)     #Randomly chose a number from 0 to 2
if user_decision <0 or user_decision>2:      #In case user typed invalid number
  print("You typed an invalid number. Please try again.")
else:
  if random_number_chosen == 0:
    print(rock)
  elif random_number_chosen == 1:
    print(paper)
  elif random_number_chosen == 2:
    print(scissors)
#To compare user's input vs computer's input to determine winner or draw
### For draw scenarios: 
  if user_decision == random_number_chosen:
    print("Aww man, its a draw!")

### For user winning: 1)User rock, computer scissors. 2)User paper, computer rock. 3)User scissors, computer paper.
  elif user_decision == 0 and random_number_chosen == 2:
    print("Congrats! You won!")
  elif user_decision == 1 and random_number_chosen == 0:
    print("Congrats! You won!")
  elif user_decision == 2 and random_number_chosen == 1: 
    print("Congrats! You won!")
  else:
    print("You lose. Better luck next time!")