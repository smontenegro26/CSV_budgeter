

DATA_FILE = 'data.csv'
FIELDNAMES = ['date', 'transaction', 'amount', 'note']

import csv
from datetime import datetime

def load_data():
  with open(DATA_FILE, 'r', newline='') as csv_file:
    reader = csv.DictReader(csv_file,  delimiter=',')
    entries = []
    for row in reader:
      entries.append(row)      
  return entries

def view_previous_entries(entries):
  for entry in entries:
    print ('{}\t{}\t${}\t{}\t'.format(entry['date'], entry['transaction'], entry['amount'], entry['note']))
  

def display_profit_loss(entries):
  expenses = 0
  income = 0
  for entry in entries:
  
    if 'Expense' in entry['transaction']: 
      expenses += int(entry['amount'])
    elif 'Income' in entry['transaction']:
      income += int(entry['amount'])
  profit = income - expenses
  
  print(
    f"The total income is ${income} \nThe total expenses are ${expenses} \nThe current profit is ${profit}"
    )

def add_new_entry(entries):

  while True:
    date = input('Date of transaction (YYYY-MM-DD): ')
    try: 
      run = bool(datetime.strptime(date,"%Y-%m-%d"))
      if run: break
    except ValueError as err:
      print('That was not a valid date, please try again!')
    
  while True:
    amt = input('Amount: ')
    if amt.isdigit(): break
    print('That was not a valid amount, please try again!')

  while True:
    transaction = input('Describe the transaction: ')
    if transaction.isalpha(): break
    print('That was not a valid transaction type, please try again!')

  while True:
    if_income = input('Was this Income (Y/N): ')
    if 'y' in if_income.lower():
      trans = 'Income'
      break
    elif 'n' in if_income.lower():
      trans = 'Expense'
      break
    print('That was not a valid choice, please try again!')

  row = dict(zip(FIELDNAMES, [date, trans, amt, transaction]))

  with open(DATA_FILE, 'a', newline='') as csv_file:
    writer = csv.DictWriter (csv_file, FIELDNAMES)
    writer.writerow(row)

  return entries.append(row)


# ===========================================
# =    Do Not Modify Anything Below Here    =
# ===========================================

def get_menu_choice():
  choice = None
  
  while choice == None:
    try:
      choice = int(input('> '))
    except ValueError as err:
      print('That was not a valid entry, please try again!')
      continue

    if choice < 1 or choice > 4:
      print('That was not a valid choice, please try again!')
      choice = None

  return choice

def print_menu():
  print('\nWhat would you like to do?\n')
  print('1) View previous entries')
  print('2) Display the current profit/loss')
  print('3) Add a new entry')
  print('4) Exit\n')

def main():
  print('====================')
  print('Welcome to Budgeter!')
  print('====================')

  entries = load_data()

  while True:
    print_menu()
    menu_choice = get_menu_choice()

    if menu_choice == 1:
      view_previous_entries(entries)
    elif menu_choice == 2:
      display_profit_loss(entries)
    elif menu_choice == 3:
      add_new_entry(entries)
    elif menu_choice == 4:
      break

main()