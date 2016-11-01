from abc import ABCMeta, abstractmethod


class BankAccount(object):
    """
        BankAccount Abstract Base Class that allows us to abstract account functions
    """

    __metaclass__ = ABCMeta
    minimum_balance = 0

    def __init__(self, holder, number, balance):
        super(BankAccount, self).__init__()
        self.Holder = holder
        self.Number = number
        self.Balance = balance

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, balance):
        # Don't set up account if minimum balance requirement for account type not met
        if not balance >= self.minimum_balance:
            raise Exception("The minimum balance for this account is %d" % self.minimum_balance)
        self._Balance = balance

    def deposit(self, amount):
        self._Balance += amount

    def withdraw(self, amount):
        # Don't withdraw beyond the minimum balance for account type
        if amount > self._Balance - self.minimum_balance:
            raise Exception("You cannot withdraw %d. Insufficient funds." % amount)
        else:
            self._Balance -= amount

    def balance(self):
        print self._Balance

    @abstractmethod
    def account_type(self):
        """"Returns a string representing the type of account this is"""
        pass


class CurrentAccount(BankAccount):
    """
        CurrentAccount has a minimum balance of 1000
    """

    minimum_balance = 1000

    def account_type(self):
        return 'current'


class SavingsAccount(BankAccount):
    """
        SavingsAccount has a minimum balance of 5000
    """

    minimum_balance = 5000

    def account_type(self):
        return 'savings'
