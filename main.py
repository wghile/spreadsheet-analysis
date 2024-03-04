# Required Tasks

    # 1. Read the data from the spreadsheet
import csv
print('\n\nSales Data')
field_names = ['year', 'month', 'sales', 'expenditure']
with open('Project/sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    # 2. Collect all of the sales from each month into a single list
print('\nList of All Sales')
print('-----------------')
with open('Project/sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    lst1 = []
    for row in spreadsheet:
        lst1.append(row)
    print(lst1)

    # 3. Output the total sales across all months
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
months_dict = []
for i in range(0, len(months)):     # Creating list of dictionaries for each month
    months_dict.append(dict(month = months[i]))   # Challenge: syntax
    months_dict[i]['total_sales'] = 0       # Challenge: using == instead of =
    months_dict[i]['total_expenditure'] = 0
# print(f'\n{months_dict}')
print('\nSummary of Total Sales per Month in 2018')
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
    print('\nMonths with Net Loss')
    print('--------------------')
    for item in net_loss:
        print(item['month'].capitalize())
    print('\nMonths with Net Income')
    print('--------------------')
    for item in net_income:
        print(item['month'].capitalize())


# Different Data Source (IMDb Movies)
import pandas as pd     #  import pandas Python Data Analysis Library

print('\n\n\nIMDb Movies Data')
movies = pd.read_csv('Project/IMDbMovies-Clean.csv')
# print(movies.columns)    # Number of Columns of Original Data = 15
df = pd.DataFrame(data=movies, columns=['Title', 'Director', 'Main Genres', 'Motion Picture Rating', 'Rating (Out of 10)', 'Release Year']).dropna()

    # Finding Movie Recommendations
print('\nMovie Recommendations')
print('---------------------')
genre = input('Search by Genre(s) - limit 3: ')
genres = genre.split(',')
rating = float(input('Minimum IMDb rating out of 10: '))
year = float(input('Release Year: '))
movie_recommendations = df[(df['Rating (Out of 10)'] >= rating) & (df['Release Year'] == year)]     # Filtering data by Rating and Release Year
# print(movie_recommendations)      # Cross checking that csv file is updating
if len(movie_recommendations) == 0: 
    print('No Movies Match Search Criteria')
else:
    movie_recommendations.to_csv('Project/filtered-movies.csv')
    lst2 = []
    with open('Project/filtered-movies.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file, fieldnames=['Index', 'Title', 'Director', 'Main Genres', 'Motion Picture Rating', 'Rating (Out of 10)', 'Release Year'])
        if len(genres) == 3:
            for row in spreadsheet:
                if row['Main Genres'].__contains__(genres[0]) and row['Main Genres'].__contains__(genres[1]) and row['Main Genres'].__contains__(genres[2]):     # str
                    lst2.append(row)
        elif len(genres) == 2:
            for row in spreadsheet:
                if row['Main Genres'].__contains__(genres[0]) and row['Main Genres'].__contains__(genres[1]):
                    lst2.append(row)
        elif len(genres) == 1:
            for row in spreadsheet:
                if row['Main Genres'].__contains__(genres[0]):
                    lst2.append(row)
        if len(lst2) == 0:
            print('No Movies Match Search Criteria')
        else:
            for item in lst2:
                print(f'\n {lst2.index(item) + 1}) {item['Title']} by Director(s) {item['Director']} -- Rated {item['Motion Picture Rating']}')