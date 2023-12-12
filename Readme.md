## About

Simple spreadsheet analysis of CSV data that was a deliverable for Code First Girls Introduction to Python course. Also used IMDb data from Kaggle and pandas library to output list of movie recommendations based on inputs.

Built with Python and pandas library

## Challenges

Using pandas library was a challenge for me as this was my first time using it. With more experience and practice, I could possibly optimize this. The 3 inputs I used to filter the data was the movie genre, IMDb rating and release year. The movie genre column was a challenge because there was missing data which created two dtypes (float and object). So initially when I tried filtering the data, I would get errors from the genre filter. First step in troubleshooting was to figure out how to handle missing values which was solved by referring to the documentation. However, when I tested the filter, it was outputting empty data frames which only occurred with the genre filter. I'm not sure if this was due to syntax error or simply not knowing how to handle filtering object dtype and inexperience with dataframe data structure. To make this easier, I split the filters into two parts: 1) rating + release year filter and 2) genre filter, since I knew the first part was working. Then, I took the filtered data and converted it to a csv file to be able to iterate over the rows in the spreadsheet and filter by genre keyword(s). Combining these two filters worked!

## Resources

- Installing Pip (Python package manager): https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter, https://stackoverflow.com/questions/60309393/how-to-install-requests-in-python-3-7-on-mac

- Pandas: https://pandas.pydata.org/docs/getting_started/index.html

- Adding key value pair to dictionary: https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/
