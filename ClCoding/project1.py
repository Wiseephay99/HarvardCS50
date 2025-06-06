#   Expense Tracker
# Daily Expenses Tracker
'''  
  - Add expenses
  - View expenses
  - Delete expenses
  - Update expenses
  - View expenses by category
  - View expenses by date
  - View expenses by amount
  - View expenses by description
  - View expenses by category
  - View expenses by date 
'''
expenses = []

print(f'\n--------Expense Tracker---------\n')


def add_expenses(description, amount):
    expenses.append({'description': description, 'amount': amount})


def view_expenses():
    for expense in expenses:
        print(f"{expense["description"]}: ${expense['amount']}")


def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f'\n---------------------------------')
    print(f"Total expenses: ${total}")
    print(f'---------------------------------\n')


add_expenses('Lunch', 10.00)
add_expenses('Transport', 5.00)
view_expenses()

calculate_total()

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


def add_expenses(description, amount):
    expenses.append({'description': description, 'amount': amount})


def view_expeses():
    for expense in expenses:
        print(f'{expense["description"]}: ${expense["amount"]}')


def calculate_total():
    total = 0
    for expense in expenses:
        total = total + expense['amount']
    print(f'Total expenses: ${total}')


input_expense = input(
    'Enter your expense and amount separated by colon(:) ..\n')
expense = input_expense.split(':')
add_expenses(expense[0], expense[1])
view_expenses()
