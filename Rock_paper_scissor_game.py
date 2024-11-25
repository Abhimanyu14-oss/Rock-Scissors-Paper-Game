'''Workflow of project:
1) Input from the user
2) computer choice(comp will choose randomly)
3) result print

Cases:
A)Rock
Rock-Rock=tie
rock-paper=paper
rock-scissor=rock
B)Paper
paper-paper=tie
paper-scissor=scissor
paper-rock=paper
C)Scissor
scissor-scissor=tie
scissor-paper=scissor
scissor-rock=rock



print("ROCK,Paper,Scissor GAME")

import random
items=["Rock","paper","Scissors"]
#print(items)
user_choice=input("enter ur choice==>")
comp_choice=random.choice(items)
print(f" user choose {user_choice}, computer choose {comp_choice}")
if user_choice==comp_choice:
    print("both chooses same items = Match Tie")
elif user_choice=="Rock" and comp_choice=="Paper":
    print("Comp Won")
elif user_choice=="Rock" and comp_choice=="Scissors":
    print("You won")
elif user_choice=="Paper" and comp_choice=="Rock":
    print("You won")
elif user_choice=="Paper" and comp_choice=="Scissors":
    print("Comp Won")
elif user_choice=="Scissors" and comp_choice=="Rock":
    print("Comp Won")
elif user_choice=="Scissors" and comp_choice=="Paper":
    print("You won")'''

    


