class Budget():
    
    filename = 'budget.txt'
    def __init__(self):
        self.transactions = self.read_file()


    def add_expence_income(self, status, value):
        self.transactions[status] = value
        self.save_file()
        print("Expense or income was added")


    def save_file(self):
        with open(self.filename, 'w') as file:
            for status, value in self.transactions.items():
                file.write(f"{status}/ {value}")
        print("File saved")


    def read_file(self):
        transactions = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    status, value = line.strip().split('/ ')
                    transactions[status] = value
        except FileNotFoundError:
            pass
        return transactions


    def summary(self):
        pass


    def display_transactions(self):
        pass



budget = Budget()

while True:
    choise = input("Enter your choise:\n1. Add an expense/income\n2. Generate a summary of expenses and revenue\n3. View transaction history\n4. Quit\n")
    if choise == '1':
        status = input("Enter the status of the transaction(+/-): ")
        value = input("Enter a value of ")
    elif choise == '2':
        pass
    elif choise == '3':
        pass
    elif choise == '4':
        break
    else:
        print("Incorrect input please enter a valid number(1-4)")