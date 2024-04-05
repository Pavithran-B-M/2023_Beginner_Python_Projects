# add updates the program to track expenditure as time goes on (page 174-175)

class BudgetManager: 

    def __init__(self, amount):
        self.available = amount
        self.budgets = {} # creates a dictionary for set budget amounts
        self.expenditure = {} # creates a dictionary for expenditure

    def add_budget(self, name, amount) :

        if name in self.budgets: #checks if the inputed parameter name is in the  budget dictionary as an exisiting key 
            raise ValueError("Budget Exists") # the following line code is used to notify the user that they already added a budget with the same name twice

        if amount > self.available: #compares the amount parameter to the global "availalbe" variable to prevent overbudgeting
            raise ValueError("Insufficient Funds")

        self.budgets[name] = amount # adding the parameter name (key) and amount (value) to the budget dictionary
        self.available -= amount # the same as saying avaible = available - amount ~ the new available amount is presented after deductions
        self.expenditure[name] = 0 #sets the added budget spendings to zero, assume the budget is new and money has not yet been spent

        return self.available 

    def spend(self, name, amount) :
        if name not in self.expenditure:
            raise ValueError ("No such budget")
        
        self.expenditure[name] += amount # will add the spent amount on a budget by adding the amount to value of the key in expenditure dictionary 

        budgeted = self.budgets[name] # collects the value of the name parameter (collects the information from budgets dictionary)

        spent = self.expenditure[name] # collects the value for the name parameter (collects information from expenditure dictionary)

        return budgeted - spent # returns the remaining available amount for the particular budget (negative values being returned indicates overbudgeting)

    def print_summary(self):

        print("Budget            Budgeted      Spent  Remaining")
        print("--------------- ---------- ---------- ----------")

        total_budgeted = 0
        total_spent = 0
        total_remaining = 0 


        for name in self.budgets: #loops through the names in the budgets dictionary 

            budgeted = self.budgets[name] #sets a variable to the set budget for the corresponding name from budgets dict.

            spent = self.expenditure[name] #sets a variable to the spent amount for the corresponding name from expenditure dict.

            remaining = budgeted - spent 

            print(f'{name:15s} {budgeted:10.2f} {spent:10.2f}' f'{remaining:10.2f}') # each name will be looped through in the budgets dictonary and a summary will be printed/ number of rows = number of keys in budgets dictonary

            total_budgeted += budgeted #adds each budgeted value for the corresponding key (name) to variable total_budgeted with each iteration of the next key in budgets dictionary

            total_spent += spent

            total_remaining += remaining
        
        print("--------------- ---------- ---------- ----------")
        print(f'{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f} {total_budgeted - total_spent:10.2f}') 

            # line 51 is space-sensitive/ after each format specifier there should be no spaces 

        


# Testing Block

outgoings = BudgetManager(2660) # assuming the full 40 hours work each week


outgoings.add_budget("Rent", 1320) # amount to provide for rent is dependent on each month (previously provided 350)
outgoings.add_budget("Groceries", 400) # assumming the amount spent $100/week 
outgoings.add_budget("Bills-phone", 220) # $100 for Shanu and 120 for me 
outgoings.add_budget("Bills-netflix", 20) # Automated withdrawl every 8th of the month
outgoings.add_budget("Bills-internet", 120) # Due every 20th of each month  
outgoings.add_budget("Bills-OSAP", 61) # Due the 31st of December
outgoings.add_budget("Bills-dental", 250)
outgoings.add_budget("Bills-CIBC CC", 50)

outgoings.spend("Rent", 1320)
outgoings.spend("Groceries", 200)
outgoings.spend("Bills-phone", 220)
outgoings.spend("Bills-netflix", 20)
outgoings.spend("Bills-dental", 250)



outgoings.print_summary()
