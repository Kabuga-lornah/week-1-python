import random

def rock_paper_scissor(rounds=5):
    choices = ['rock', 'paper', 'scissors']
    computer_score = 0
    user_score = 0
    round_count = 0  

    while round_count < rounds:
        computer_choice = random.choice(choices)
        user_choice = input('Enter rock, paper, or scissors: ').lower()

        if user_choice not in choices:
            print('Invalid choice')
            continue
      
        print(f"Computer chose: {computer_choice}") #f string

        if user_choice == computer_choice:
            print("It's a tie.")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            user_score += 1
            print("You win this round.")
        else:
            computer_score += 1
            print("Computer wins this round.")

        round_count += 1  
        print(f"Score - You: {user_score}, Computer: {computer_score}")

       
        if rounds == 5 and (user_score == 3 or computer_score == 3):
            break

  
    if user_score > computer_score:
        print("You won the game.")
    elif computer_score > user_score:
        print("Computer won the game.")
    else:
        print("The game is a tie.")


rock_paper_scissor(5)
