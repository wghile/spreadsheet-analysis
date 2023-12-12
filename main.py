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

print('\n\n\nIMDb Movies')
movies = pd.read_csv('Project/IMDbMovies-Clean.csv')
# print(movies.columns)    # Number of Columns of Original Data = 15
df = pd.DataFrame(data=movies, columns=['Title', 'Director', 'Main Genres', 'Motion Picture Rating', 'Rating (Out of 10)', 'Release Year']).dropna()

# movies = data.to_csv('Project/IMDbMovies.csv')

# with open('Project/IMDbMovies.csv', 'r') as csv_file:
#     spreadsheet = csv.DictReader(csv_file)
#     for row in spreadsheet:
#         print(row)

    # Testing different methods on data
# print(movies)   # displays first and last 5 rows
# print(movies.head(2))   # displays first 2 rows
#print(movies.tail(2))   # displays last 2 rows
# print(movies.columns)   # columns of data
# print(movies['Title'].shape)    # number of rows

## Movie Recommendations
print('\nMovie Recommendations')
print('---------------------')
# headers = movies.columns
# print(len(movies))
# print(headers)
# print(movies['Main Genres'].info)
genre = input('Search by Genre: ')
rating = float(input('Minimum IMDb rating out of 10: '))
year = float(input('Release Year: '))
movie_recommendations = df[(df['Rating (Out of 10)'] >= rating) & (df['Release Year'] == year)]
print(movie_recommendations['Main Genres'])
# new_movies = []
# print(movies['Main Genres'].fillna('Missing')[4578])
# movies['Main Genres'].dropna()
# movies.drop(['Number of Ratings (in thousands)'], axis=1)
# print(movies)
# print(movies['Main Genres'][50].split(',').__contains__('Action'))
# print(movies['Main Genres'][25].split(','))
# new_movies = movies['Main Genres'].notna()
# print(new_movies['Title'] == 'Gran Torino')
# movie_pass = movies.loc[(movies['Main Genres'] == genre), ['Title','Director']]
# print(movies['Main Genres'][7518])
    # print(f'{movie['Title'].to_string(index=False)} by Director {movie['Director'].to_string(index=False)}')
# print(movies['Main Genres'].info())


# print(new_movies['Main Genres'][5320])
# print(movies['Main Genres'][5320])
# print(movies['Main Genres'][9082])
# print(movies)
# for movie in movies:
    # print(movie)
# if movies['Main Genres'][0].__contains__('Action'):
#     print('Yes')
# for i in range(0, len(movies)):
#     # is_genre = type(movies['Main Genres'][i]) == str
#     movies_with_genres = movies[movies['Main Genres'][i].dtype]
    # movies_with_genres = movies['Main Genres'][i].dtypes == str
# print(len(movies_with_genres))
    # if type(movies['Main Genres'][i]) == str:
    #     new_movies.append(movies[i])
    # if is_genre:
    #     print(movies['Main Genres'])
# print(movies[movies['Release Year'] > 2022])
# answer = movies[(movies['Release Year'] > 2022) & (is_genre)]
# print(type(answer['Main Genres']))
# movie_recommendations = []
# new_movies = []
# for i in range(0, len(movies)):
# movies_with_genres = movies['Main Genres'].notna()
# print(len(movies_with_genres))
# for movie in movies:
#     print(movie)
    # if movies_with_genres:
    #     new_movies.append(movie)
# print(len(new_movies))
# print(new_movies)
    # print(type(movies['Main Genres'][i]))
#     if type(movies['Main Genres'][i]) == float:
#         print(i)
# print(type(movies['Main Genres'][0]) == str)
# print(movies['Main Genres'][4578])
# print(movies['Main Genres'][5320])
# print(movies['Main Genres'][6743])
# print(movies['Main Genres'][7518])
# print(movies['Main Genres'][7909])
# print(movies['Main Genres'][8323])
# print(movies['Main Genres'][8558])
    # if type(movies['Main Genres'][i]) == str:
    # is_genre = movies['Main Genres'][i].__contains__(genre) == True & type(movies['Main Genres'][i] == str)
# if is_genre:

# movie_pass = movies[(movies['Main Genres'][i].__contains__(genre) == True) & (movies['Rating (Out of 10)'] >= rating) & (movies['Release Year'] == year)]
# print(movie_pass)
    # movie_recommendations.append(movie_pass)
# print(movie_recommendations)
# movie_list = []
# movie_list.append(movie_recommendation['Title'])
# if len(movie_list) > 0:
#     print(movie_list)
# else:
#     print('No Movies Found That Match Criteria')
