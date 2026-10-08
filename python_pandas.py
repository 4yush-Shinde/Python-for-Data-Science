# Pandas - A powerful data manipulation and analysis library for Python.
# It provides data structures like DataFrames and Series, which allow for efficient handling of structured data.
# Pandas is widely used in data science, machine learning, and statistical analysis.


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