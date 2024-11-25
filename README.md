Rock, Paper, Scissors Game 🎮

A simple and fun Python project that simulates the classic Rock, Paper, Scissors game. Test your luck and strategy against the computer!

🚀 Features
Interactive Gameplay: Choose between Rock, Paper, or Scissors and see how your choice stacks up against the computer's random pick.
Randomized Computer Moves: The computer's choice is generated randomly for a fair game.
Immediate Results: Instantly see if you won, lost, or tied with the computer.

🛠️ Workflow of the Project
1️⃣ User Input: Enter your choice: Rock, Paper, or Scissors.
2️⃣ Computer's Choice: The computer selects its move randomly.
3️⃣ Determine the Winner: Based on the classic rules of the game:

Rock vs Scissors: Rock wins 🪨✂️
Paper vs Rock: Paper wins 📄🪨
Scissors vs Paper: Scissors wins ✂️📄
4️⃣ Result Announcement: The winner is displayed instantly!
🧠 Rules of the Game
Rock 🪨
Rock vs Rock = Tie
Rock vs Paper = Paper Wins
Rock vs Scissors = Rock Wins
Paper 📄
Paper vs Paper = Tie
Paper vs Rock = Paper Wins
Paper vs Scissors = Scissors Wins
Scissors ✂️
Scissors vs Scissors = Tie
Scissors vs Paper = Scissors Wins
Scissors vs Rock = Rock Wins


📄 Code Implementation
Here's a sneak peek at the main code logic:

python

import random

print("ROCK, PAPER, SCISSORS GAME")

items = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
comp_choice = random.choice(items)

print(f"User chose {user_choice}, Computer chose {comp_choice}")

if user_choice == comp_choice:
    print("Both chose the same item = Match Tie!")
elif user_choice == "Rock" and comp_choice == "Paper":
    print("Computer Won!")
elif user_choice == "Rock" and comp_choice == "Scissors":
    print("You Won!")
elif user_choice == "Paper" and comp_choice == "Rock":
    print("You Won!")
elif user_choice == "Paper" and comp_choice == "Scissors":
    print("Computer Won!")
elif user_choice == "Scissors" and comp_choice == "Rock":
    print("Computer Won!")
elif user_choice == "Scissors" and comp_choice == "Paper":
    print("You Won!")
    
💻 How to Run the Game
Clone the repository:
bash

git clone https://github.com/your-username/rock-paper-scissors-game.git
Navigate to the project directory:
bash

cd rock-paper-scissors-game
Run the Python script:
bash

python rock_paper_scissors.py

Created BY: Abhimanyu Rana
email: abhimanyurana39@gmail.com
LinkedIN : www.linkedin.com/in/abhimanyurana39
