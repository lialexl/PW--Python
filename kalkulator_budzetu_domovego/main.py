class Budget():
    
    filename = 'budget.txt'
    def __init__(self):
        self.transactions = self.read_file()


    def add_expence_income(self, status, value):
        self.transactions.append(status)
        self.transactions.append(value)
        self.save_file()
        print("Expense or income was added")


    def save_file(self):
        with open(self.filename, 'w') as file:
            i=0
            while i < len(self.transactions):
                file.write(f"{self.transactions[i]}")
                i+=2
        print("File saved")


    def read_file(self):
        transactions = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    status, value = line.strip().split('/ ')
                    transactions.append(status)
                    print(status)
                    transactions.append(value)
                    print(value)
        except FileNotFoundError:
            pass
        return transactions


    def summary(self):
        revenue = 0
        expenses = 0


    def display_transactions(self):
        i=0
        while i < len(self.transactions):
            print(self.transactions[i], end= '')
            i+=1
            print(self.transactions[i])
            i+=1

        



budget = Budget()

while True:
    choise = input("Enter your choise:\n1. Add an expense/income\n2. Generate a summary of expenses and revenue\n3. View transaction history\n4. Quit\n")
    if choise == '1':
        status = input("Enter the status of the transaction(+/-): ")
        value = input("Enter a value of the transaction")
        budget.add_expence_income(status, value)
    elif choise == '2':
        pass
    elif choise == '3':
        budget.display_transactions()
    elif choise == '4':
        break
    else:
        print("Incorrect input please enter a valid number(1-4)")