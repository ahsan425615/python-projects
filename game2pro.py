import random

def show_instructions():
    print("Welcome to the Number Guessing Game!")
    print("====================================")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible.")
    print("Type 'quit' to exit the game.")

def main():
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    
    show_instructions()
    
    while True:
        guess = input("Enter your guess: ")
        
        if guess.lower() == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        number_of_attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {number_of_attempts} attempts.")
            break

if __name__ == "__main__":
    main()








