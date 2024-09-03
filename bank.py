class Bank:
    def __init__(self) -> None:
        self.account = {}

    def account_creation(self, name, account_no, balance):
        if account_no not in self.account:
            if balance >= 100:  # Ensuring the minimum balance condition
                self.account[account_no] = {
                    "name": name,
                    "balance": balance,
                }
                print("Account successfully created")
                print("WELCOME TO HDFC BANK")
            else:
                print("Minimum balance of 100 is required to create an account")
        else:
            print("Account number already exists. Please try another one.")

    def deposit(self, account_no, amount):
        if account_no in self.account:
            if amount > 0:
                self.account[account_no]["balance"] += amount
                print(f"Amount {amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")
        else:
            print("Enter a valid account number.")

    def withdrawal(self, account_no, amount):
        if account_no in self.account:
            if amount > 0:
                if self.account[account_no]["balance"] >= amount:
                    self.account[account_no]["balance"] -= amount
                    print(f"Amount {amount} withdrawn successfully.")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("Enter a valid account number.")

    def balance(self, account_no):
        if account_no in self.account:
            return f"Account Balance: {self.account[account_no]['balance']}"
        else:
            return "Enter a valid account number."

    def account_details(self, account_no):
        if account_no in self.account:
            return self.account[account_no]
        else:
            return "Enter a valid account number."


bank1 = Bank()

while True:
    print(
        """\nChoose an option:
        1: Account creation
        2: Bank Details
        3: Account Balance
        4: Cash deposit
        5: Cash withdrawal
        6: Exit"""
    )

    a = int(input("Enter your choice: "))

    if a == 1:
        name = input("Enter name: ")
        account_no = int(input("Enter a 5-digit account number: "))
        balance = float(
            input("Deposit a minimum of 100 rupees as the first transaction: ")
        )
        bank1.account_creation(name, account_no, balance)

    elif a == 2:
        account_no = int(input("Enter a valid 5-digit account number: "))
        details = bank1.account_details(account_no)
        print(details)

    elif a == 3:
        account_no = int(input("Enter a valid 5-digit account number: "))
        balance = bank1.balance(account_no)
        print(balance)

    elif a == 4:
        account_no = int(input("Enter a valid 5-digit account number: "))
        cash = float(input("Enter the amount to deposit: "))
        bank1.deposit(account_no, cash)

    elif a == 5:
        account_no = int(input("Enter a valid 5-digit account number: "))
        cash = float(input("Enter the amount to withdraw: "))
        bank1.withdrawal(account_no, cash)

    elif a == 6:
        print("Thank you for using HDFC Bank services!")
        break

    else:
        print("Invalid option. Please choose a correct one.")
