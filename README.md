## Project Brief

This is a simple banking application written in Python that allows
users to create a new account, login to an existing account, deposit,
withdraw, transfer and check balance. The data of all the accounts
is stored in a JSON file called 'bank_app_db.json'. The code consists of
functions to deposit and withdraw money, generate a random account
number, and implement a basic UI for interacting with the users. 
The UI uses a while loop that keeps running until the user decides to quit.
The user can log in to their account by entering the correct account number
and login pin. Once logged in, the user can perform 
operations such as withdrawal, deposit, transfer and check balance.

### Documentation

The project makes use of Pythons Data Structures,
Algorithms, Methods and makes use 
of the following functions:

`def deposit()`

- To deposit money.

`def withdraw()`

- To withdraw money if user balance is sufficient.

`def account_num()`

- To generate a random account number starting with '0'