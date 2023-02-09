import random
from datetime import datetime
import time
import json

with open('bank_app_db.json', 'r') as file:
    data = json.load(file)


def deposit(amounts: float, prev_bal: float):
    new_balance = amounts + prev_bal
    return new_balance


def withdraw(amounts: float, prev_bal: float):

    if amounts > prev_bal:
        raise ValueError("Insufficient funds")
    else:
        new_balance = prev_bal - amounts
        return new_balance


def account_num():
    otp = "0"
    for _ in range(9):
        otp += str(random.choice(range(10)))
    return otp


print("*" * 31)
print("Welcome to the Skillup Bank")
print("*" * 31)
while True:
    print("What would you like to do?\n1. Create a new account.\n2. Login to an existing account.\n3. Quit.")
    user_input = input('::>>')

    if user_input == '1':
        print("Please enter your Personal details below.")
        f_name = input('First Name:\n>')
        l_name = input('Last Name:\n>')
        pin = input('Login Pin:\n>')
        trans_pin = input('Transaction Pin:\n>')
        acc_num = account_num()
        print("Account creation processing...")
        time.sleep(2)
        print('Successful')
        time.sleep(1)

        new_account = {
            acc_num:
                {
                    'name': f"{f_name} {l_name}",
                    'pin': pin,
                    'trans_pin': trans_pin,
                    'bal': 0,
                }
        }
        data.update(new_account)
        print(
            f"""\nWelcome, {f_name}!\nYou have successfully created your Customer account.\n
            Your account number is {acc_num}.""")
    elif user_input == "2":
        with open('bank_app_db.json', 'r') as file:
            data = json.load(file)
        print("\nPlease enter your Account number.")
        acc_num = input('Account Number:\n>')
        print("\nPlease enter your secure login pin.")
        pin = input('Login Pin:\n>')

        user_data = data.get(acc_num)

        if user_data and user_data.get("pin") == pin:
            print("Login Successful")
            first_login = True
            while True:
                if first_login:
                    print(f"Welcome, {user_data['name'].split()[0].title()}")
                    first_login = False
                else:
                    print("*" * 31)
                    print(f"Welcome back, {user_data['name'].split()[0].capitalize()}")

                print(
                    "What would you like to do?\n1. Withdraw.\n2. Deposit.\n3. Transfer.\n4. Check Balance\n5. Logout")
                input_ = input(":>>")
                if input_ == "1":
                    print('Enter Withdrawal amount')
                    amount = float(input("::>"))
                    if amount > user_data['bal']:
                        print("Insufficient Funds")
                    else:
                        trans_pin = input("Transaction Pin:\n>")
                        if trans_pin == user_data['trans_pin']:
                            new_bal = withdraw(amount, user_data['bal'])
                            user_data['bal'] = new_bal
                            print(f'Your withdrawal of {amount} naira was successful')
                        else:
                            print("Incorrect Transaction pin")
                elif input_ == "2":
                    print('Enter Deposit amount')
                    amount = float(input("::>"))
                    try:
                        amt = deposit(amount, user_data['bal'])
                        user_data['bal'] = amt
                        print(f'Your deposit of {amount} naira was successful')
                    except ValueError as msg:
                        print(msg)
                elif input_ == '3':
                    other_acc = input("Enter recipient account number\n:>> ")
                    trans_amount = int(input("Enter Amount you want to Transfer\n:>> "))
                    trans_pin = input("Enter transaction pin:\n>")

                    beneficiary = data.get(other_acc)

                    if beneficiary:
                        if trans_amount > user_data['bal']:
                            print("Insufficient Funds")
                        else:
                            if trans_pin == user_data['trans_pin']:
                                user_data['bal'] -= trans_amount

                                beneficiary['bal'] += trans_amount

                                print("\nTransfer Successful")
                            else:
                                print("Incorrect pin.")
                    else:
                        print("Beneficiary not found")
                elif input_ == '4':
                    current_date = datetime.now().date()
                    date = current_date.strftime("%a, %d of %B, %Y")
                    print(f"Your current balance at {date} is {user_data['bal']} naira")

                elif input_ == "5":
                    break

        else:
            print("Invalid credentials.")
    elif user_input == "3":
        break
with open('bank_app_db.json', 'w') as file:
    json.dump(data, file, indent=4)
