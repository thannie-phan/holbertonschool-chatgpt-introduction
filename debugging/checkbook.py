#!/usr/bin/python3

class Checkbook:
    """
    Class Description:
    ------------------
    A simple Checkbook class to manage deposits, withdrawals, and balance queries.

    Attributes:
    -----------
    balance : float
        Represents the current balance of the checkbook. Initialized to 0.0.
    """

    def __init__(self):
        """Initializes a new checkbook with a balance of 0.0"""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a given amount into the checkbook.

        Parameters:
        -----------
        amount : float
            The amount of money to deposit. Must be positive.

        Returns:
        --------
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a given amount from the checkbook if sufficient funds exist.

        Parameters:
        -----------
        amount : float
            The amount of money to withdraw. Must be positive.

        Returns:
        --------
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Prints the current balance of the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main program loop for the checkbook application.

    Handles user commands: deposit, withdraw, balance, and exit.
    Includes error handling to prevent crashes from invalid input.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount < 0:
                        print("Please enter a positive amount.")
                        continue
                    cb.deposit(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount < 0:
                        print("Please enter a positive amount.")
                        continue
                    cb.withdraw(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

