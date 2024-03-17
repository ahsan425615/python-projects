import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    player_name = input("Enter your name: ")
    
    player_roll = roll_dice()
    computer_roll = roll_dice()
    
    print(f"{player_name} rolls: {player_roll}")
    print("Computer rolls:", computer_roll)
    
    if player_roll > computer_roll:
        print(f"{player_name} wins!")
    elif player_roll < computer_roll:
        print("Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()







