"""

 Program Description: Simple Bank Account Manager
  Language : Python 3
  Date Written : 12-14-2023
  Date Modified : 12-14-2023
  Programmers : Aldwin Guanzon

"""


# To Check the Current Balance
def check_balance(balance):
    print("----------------------------------")
    print(f"  Your Current Balance: ${balance}")
    print("---------------------------------\n")


# To Deposit
def to_deposit(amount, balance):
    balance += amount
    return balance


# To Withdraw
def to_withdraw(amount, balance):
    balance -= amount
    return balance


default_balance = 1000
# Input Validation and Error Handling
print("Welcome to the Simple Bank Account Manager!")
print(f"Your Current Balance: ${default_balance}")
while True:
    # User Interaction
    option = input("What would you like to do (C - Check balance | D – Deposit | W - Withdraw | E- Exit): ").upper()
    # Input Validation
    if option.upper() not in ('C', 'D', 'W', 'E'):
        print("Invalid Input. Please Enter Valid Option.\n")
        continue

    # To ext
    elif option == "E":
        print("\nThank You For Using the Simple Bank Account Manager!")
        break

    # To Check
    elif option == "C":
        check_balance(default_balance)

    # To Deposit
    elif option == "D":
        while True:
            # Input Validation
            try:
                deposit = float(input("How much would you like to deposit: $"))
                # Error Handling
                if deposit < 0:
                    print("You Can't Deposit a Negative Amount")
            except ValueError:
                print("Invalid Input. Please Enter a Numeric Value")
            else:
                print("----------------------------")
                print(f"   Current Balance: ${default_balance}")
                print(f"   Deposit: ${deposit}")
                print(f"   New Balance: ${to_deposit(deposit, default_balance)}")
                print("----------------------------\n")
                default_balance = to_deposit(deposit, default_balance)
                break

    # To Withdraw
    elif option == "W":
        while True:
            # Input Validation
            try:
                withdraw = float(input("\nHow Much Would You Like to Withdraw: $"))
                # Error Handling
                if withdraw < 0:
                    print("You Can't Withdraw a Negative Amount")
                    continue
                elif withdraw > default_balance:
                    print("Sorry, You Don't Have Sufficient Balance\n")
                    break
            except ValueError:
                print("Invalid Input. Please Enter a Numeric Value")
            else:
                print("----------------------------")
                print(f"   Current Balance: ${default_balance}")
                print(f"   Withdraw: ${withdraw}")
                print(f"   New Balance: ${to_withdraw(withdraw, default_balance)}")
                print("----------------------------\n")
                default_balance = to_withdraw(withdraw, default_balance)
                break
