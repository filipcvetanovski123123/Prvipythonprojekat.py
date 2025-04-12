def show_balance(balance):
    print(f"Your balance is {balance:.2f}")


def deposit(balance):
    amount = float(input("Enter an amount to deposit: "))
    if amount <= 0:
        print("That is not a valid deposit amount.")
    else:
        balance= balance+amount
        print(f"Deposited {amount:.2f}. New balance is {balance:.2f}")
    return balance


def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
    elif amount <= 0:
        print("Amount must be greater than zero.")
    else:
        balance -= amount
        print(f"Withdrew {amount:.2f}. New balance is {balance:.2f}")
    return balance


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            is_running = False
            print("Thank you for banking with us!")
        else:
            print("This is not a valid choice.")


if __name__ == "__main__":
    main()