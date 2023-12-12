# Required Tasks

# 1. Read the data from the spreadsheet
import csv
field_names = ['year', 'month', 'sales', 'expenditure']
with open('Project/sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

# 2. Collect all of the sales from each month into a single list
print('\nList of All Sales')
print('-----------------')
with open('Project/sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    list = []
    for row in spreadsheet:
        list.append(row)
    print(list)

# 3. Output the total sales across all months
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
months_dict = []
# months_dict = [{'month': 'jan', 'total_sales': 0}, {'month': 'feb', 'total_sales': 0}, {'month': 'mar', 'total_sales': 0}, {'month': 'apr', 'total_sales': 0}, {'month': 'may', 'total_sales': 0}, {'month': 'jun', 'total_sales': 0}, {'month': 'jul', 'total_sales': 0}, {'month': 'aug', 'total_sales': 0}, {'month': 'sep', 'total_sales': 0}, {'month': 'oct', 'total_sales': 0}, {'month': 'nov', 'total_sales': 0}, {'month': 'dec', 'total_sales': 0}]
for i in range(0, len(months)):
    months_dict.append(dict(month = months[i]))   # Challenge: syntax
    months_dict[i]['total_sales'] = 0       # Challenge: using == instead of =
    months_dict[i]['total_expenditure'] = 0
print('\n\nSummary of Total Sales per Month in 2018')
print('----------------------------------------')
with open('Project/sales.csv', 'r') as csv_file:    # Displays list of each month's total sales
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:     # Challenge: for loops reversed only updated 1st el in dict
        for i in range(0, len(months_dict)):
            if row['month'] == months_dict[i]['month']:
                months_dict[i]['total_sales'] += int(row['sales'])
                months_dict[i]['total_expenditure'] += int(row['expenditure'])
    net_loss = []
    net_income = []
    net_zero = []
    for item in months_dict:    # Categorizing months based on profit/loss
        print(f'{item['month'].capitalize()}: ${item['total_sales']}.00')
        if int(item['total_sales']) < int(item['total_expenditure']):
            net_loss.append(item)
        elif int(item['total_sales']) == int(item['total_expenditure']):
            net_zero.append(item)
        else:
            net_income.append(item)
    print('\n\nMonths with Net Loss')
    print('--------------------')
    for item in net_loss:
        print(item['month'].capitalize())
    print('\nMonths with Net Income')
    print('--------------------')
    for item in net_income:
        print(item['month'].capitalize())


# Different Data Source (IMDb Movies)
import pandas as pd     #  import pandas Python Data Analysis Library

print('\n\nIMDb Movies')
movies = pd.read_csv('Project/IMDbMovies-Clean.csv')
# print(movies.columns)    # Number of Columns of Original Data = 15
df = pd.DataFrame(data=movies, columns=['Title', 'Director', 'Main Genres', 'Motion Picture Rating', 'Rating (Out of 10)', 'Release Year']).dropna()

## Movie Recommendations
print('\nMovie Recommendations')
print('---------------------')
genre = input('Search by Genre(s): ')
rating = float(input('Minimum IMDb rating out of 10: '))
year = float(input('Release Year: '))
movie_recommendations = df[(df['Rating (Out of 10)'] >= rating) & (df['Release Year'] == year)]     # Filtering data by Rating and Release Year
# print(movie_recommendations)      # Cross checking that csv file is updating
if len(movie_recommendations) == 0: 
    print('No Movies Found that Match Search Criteria')
else:
    movie_recommendations.to_csv('Project/recommendations.csv')
    list = []
    with open('Project/recommendations.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file, fieldnames=['Index', 'Title', 'Director', 'Main Genres', 'Motion Picture Rating', 'Rating (Out of 10)', 'Release Year'])
        for row in spreadsheet:
            if row['Main Genres'].__contains__(genre):
                list.append(row)
        for item in list:
            print(f'\n {list.index(item) + 1}) {item['Title']} by Director(s) {item['Director']}')