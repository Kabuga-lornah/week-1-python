import random

def rock_paper_scissor():
    choices = ['rock', 'paper', 'scissors']
    

    while True:
        while True:
            rounds_input = input("How many rounds do you want to play? Enter 3 or 5: ")
            if rounds_input in ['3', '5']:
                rounds = int(rounds_input)
                break
            else:
                print("Please enter either 3 or 5.")

        computer_score = 0
        user_score = 0
        round_count = 0
        win_score = rounds // 2 + 1  

        print(f"\nGame start! First to {win_score} wins out of {rounds} rounds.")

        while round_count < rounds:
            print("\nChoices: rock, paper, or scissors")
            user_choice = input("Enter your choice: ").strip().lower()

            if user_choice not in choices:
                print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
                continue

            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")

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

          
            if user_score == win_score or computer_score == win_score:
                break

        print("\nGame Over!")
        if user_score > computer_score:
            print("You won the game!")
        elif computer_score > user_score:
            print("Computer won the game!")
        else:
            print("The game is a tie!")

      
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

rock_paper_scissor()
