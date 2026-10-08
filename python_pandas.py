# YouTube Video: https://youtu.be/VXtjG_GzO7Q
# Pandas - A powerful data manipulation and analysis library for Python.
# It provides data structures like DataFrames and Series, which allow for efficient handling of structured data.
# Pandas is widely used in data science, machine learning, and statistical analysis.


#################################### Series ############################################
# Series - A one-dimensional labeled array capable of holding any data type 
# (integers, strings, floating point numbers, Python objects, etc.). 
# It is similar to a column in a spreadsheet or a SQL table.


import pandas as pd
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)




# It prints the index and the corresponding values of the Series.
# We can also access individual elements using their index.
print(series[0])  # Accessing the first element
print(series[2])  # Accessing the third element




# We can also create a Series with custom indices.
custom_index_series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(custom_index_series)




# Dictionary data can also be used to create a Series, where the keys become the index and the values become the data.
calories_data = {'Day 1': 1750, 'Day 2': 2000, 'Day 3': 2150, 'Day 4': 1700, 'Day 5': 2200}
series_from_dict = pd.Series(calories_data)
print(series_from_dict)

# We can also locate elements in the Series using their index labels.
print(series_from_dict.loc['Day 1'])  # Loc stands for location and is used to access a group of rows and columns by labels or a boolean array.




#################################### DataFrames ############################################
# DataFrame - A two-dimensional labeled data structure with rows and columns of potentially different types.
# It is similar to a spreadsheet or SQL table.

data = {
    'Name': ['Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data, index = ['Employee 1', 'Employee 2', 'Employee 3']) # Custom Index
print(df)


# Adding a new column to the DataFrame
df['Salary'] = [50000, 60000, 70000] # The values in the new column must match the number of rows in the DataFrame.
print(df)


# Adding a new row to the DataFrame
# Creating a new DataFrame for the new row with the same columns as the existing DataFrame.

new_row = pd.DataFrame({'Name': ['John'], 'Age': [28], 'City': ['San Fran'], 'Salary': [80000]}, index=['Employee 4']) # We have also provided a custom index for the new row.

# Remember that we can add multiple rows at once by providing a list of dictionaries or a DataFrame with multiple rows.
new_row2 = pd.DataFrame([{'Name': 'John', 'Age': 28, 'City': 'San Fran', 'Salary': 80000},
                        {'Name': 'Jim', 'Age': 30, 'City': 'Boston', 'Salary': 62000}], index=['Employee 4', 'Employee 5'])

df = pd.concat([df, new_row2]) # Concatenating the new row to the existing DataFrame.
print(df)