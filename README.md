#BankAccount Class

GitHub repo containing a real-world problem modeled using OOP while taking advantage of inheritance, encapsulation, polymorphism and the other OOP concepts.

Class has two account types: Current and Savings

Current account has a minimum balance of 1,000

Savings account has a minumum balance of 5,000

##Usage
Account creation function takes three parameters in this order: Account holder name, account number, opening balance

Create current account

	account = BankAccount.CurrentAccount('A. N. Other', 1234, 5000)

Create savings account

	account = BankAccount.SavingsAccount('A. N. Other', 1234, 5000)

Deposit amount into account

	account.deposit(1000)

Withdraw from account

	account.withdraw(1000)

Get account balance

	account.balance()