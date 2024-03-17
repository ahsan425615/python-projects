class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def check_balance(self):
        print(f"Account balance for {self.name}: ${self.balance}")


def main():
    print("Welcome to the Bank Account Management System!")
    name = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance: $"))

    # Create a new bank account
    account = BankAccount(name, initial_balance)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: $"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using the Bank Account Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
