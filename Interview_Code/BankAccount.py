class BankAccount:
    def __init__(self):
        self.balance = 0

    def balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def main(self):
        while True:
            print("\nPlease make a selection:")
            print("1: Check Balance")
            print("2: Make Withdrawal")
            print("3: Make Deposit")
            print("4: Close session")

            selection = int(input())

            if selection == 1:
                limited_cur_balance = "{:.2f}".format(self.balance)
                print("\nYour current account balance is: $" + str(limited_cur_balance))

            elif selection == 2:
                withdraw = float(input("Enter an Amount to Withdraw: "))
                if withdraw < self.balance:
                    self.withdraw(withdraw)
                    limited_withdraw = "{:.2f}".format(self.balance)
                    print("\nYour new balance is: $" + str(limited_withdraw))
                else:
                    print("\nYour desired withdrawal amount exceeds your account balance.")
            elif selection == 3:
                deposit = float(input("Enter an Amount to Deposit: "))
                self.deposit(deposit)
                limited_deposit = "{:.2f}".format(self.balance)
                print("\nYour new balance is: $" + str(limited_deposit))
            elif selection == 4:
                limited_balance = "{:.2f}".format(self.balance)
                print("\nYour final account balance is: $" + str(limited_balance))
                print("Exiting account, thank you for your business!")
                return
            else:
                print("\nPlease make a selection from the above list.")


BA = BankAccount()

BA.main()
