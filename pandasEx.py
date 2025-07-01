# Why We Use Pandas
# Pandas is a Python library used for data analysis and manipulation. It makes working with structured data (like tables and Excel files) much easier and more powerful.
# ✅ Key Uses:
# Reading & Writing Data (CSV, Excel, JSON, SQL, etc.)
# Cleaning & Filtering messy data
# Performing calculations on data (sum, mean, group, etc.)
# Handling missing data  

import pandas as pd

data = pd.read_csv('E:\\py\\python-main\\archive\\Trending_Movies.csv')
print(data.head())  # Shows the first 5 rows

vote_counts = data[data['vote_count'] > 100]
print(vote_counts)