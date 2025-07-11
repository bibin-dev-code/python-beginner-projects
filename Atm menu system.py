# Simple ATM Simulator

balance = 1000  # Starting balance
pin = "1234"  # Default PIN

# Login step
user_pin = input("Enter your 4-digit PIN: ")

if user_pin != pin:
    print("Incorrect PIN ❌")
else:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your balance is ₹{balance}")

        elif choice == "2":
            deposit = int(input("Enter amount to deposit: ₹"))
            balance += deposit
            print(f"₹{deposit} added successfully. New balance: ₹{balance}")

        elif choice == "3":
            withdraw = int(input("Enter amount to withdraw: ₹"))
            if withdraw > balance:
                print("Insufficient balance 😓")
            else:
                balance -= withdraw
                print(f"₹{withdraw} withdrawn. Remaining balance: ₹{balance}")

        elif choice == "4":
            print("Thank you for using BibinBank™ ATM 💼")
            break

        else:
            print("Invalid choice. Please select 1 to 4.")
