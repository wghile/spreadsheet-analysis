# Required Tasks

# 1. Read the data from the spreadsheet
import csv
field_names = ['year', 'month', 'sales', 'expenditure']
with open('Project/sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

# 2. Collect all of the sales from each month into a single list
print(f'\nList of All Sales')
print(f'-----------------')
with open('Project/sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    list = []
    for row in spreadsheet:
        list.append(row)
    print(list)

# 3. Output the total sales across all months
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
months_dict = [{'month': 'jan', 'total_sales': 0}, {'month': 'feb', 'total_sales': 0}, {'month': 'mar', 'total_sales': 0}, {'month': 'apr', 'total_sales': 0}, {'month': 'may', 'total_sales': 0}, {'month': 'jun', 'total_sales': 0}, {'month': 'jul', 'total_sales': 0}, {'month': 'aug', 'total_sales': 0}, {'month': 'sep', 'total_sales': 0}, {'month': 'oct', 'total_sales': 0}, {'month': 'nov', 'total_sales': 0}, {'month': 'dec', 'total_sales': 0}]
print(f'\n\nSummary of Total Sales per Month in 2018')
print(f'----------------------------------------')
with open('Project/sales.csv', 'r') as csv_file:    # Displays list of each month's total sales
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        for i in range(0, len(months_dict)):
            if row['month'] == months_dict[i]['month']:
                months_dict[i]['total_sales'] += int(row['sales'])
    print(months_dict)
month = input('\nWhat month do you want to see total sales for? (3 letter abbrv) ').lower()
sales = 0
for object in months_dict:      # Displays certain month's total sales
    if object['month'] == month:
        print(f'The total sales for the month of {month.capitalize()} was ${object['total_sales']}.00\n')