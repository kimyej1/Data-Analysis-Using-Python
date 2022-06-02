###########################################################
### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###
###########################################################

import imp, os, sys
sol = imp.load_compiled("solutions", "./solutions.py")
sol.get_solutions("imdb.xlsx")
from nose.tools import assert_equal
from pandas.util.testing import assert_frame_equal, assert_series_equal

# Loading the data
import pandas as pd

xls = pd.ExcelFile('imdb.xlsx')
df = xls.parse('imdb')
df_directors = xls.parse('directors')
df_countries = xls.parse('countries')

df = pd.merge(left=df, right=df_countries,
              how='inner', left_on='country_id',
              right_on='id')

df = pd.merge(left=df, right=df_directors,
              how='inner', left_on='director_id',
              right_on='id')

print("Finished.")

""" Q1: 
Get the summary statistics for imdb_score and gross, then use the describe() function to summarize this visually. Save the
result in a variable called score_gross_description and print it.
"""

# your code here
score_gross_description = df[["imdb_score", "gross"]].describe()
print(score_gross_description)


"""Q2:
What is the average rating of the director Christopher Nolan's movies? Save this value in a variable called nolan_mean and 
print.
"""

# your code here
nolan_mean = (df[df["director_name"] == "Christopher Nolan"])["imdb_score"].mean()
print(nolan_mean)

"""Q3: 
Create a series called 'directors' that contains each director's name and his or her average rating.  
Print out the type of your variable.
Use the 'directors' series to find the average rating for Steven Spielberg.  Print the value.
"""

# your code here
directors = df.groupby("director_name")["imdb_score"].mean()
print(type(directors))

"""Q4:
Select the non-USA movies made after 1960 by Hayao Miyazaki.
Save the result in a DataFrame called 'miyazaki', then print it.

Here are the steps:
1. Query the data ('df' DataFrame) based on the following conditions:
- Non-USA movies (country_id != 1)
- Movies made after 1960 (title_year > 1960)
- Movies made by director Hayao Miyazaki (director_id == 46)
2. Save the filtered data in a DataFrame called 'miyazaki' and print it

"""

# your code here
miyazaki = df[df["country_id"] != 1][df["title_year"] > 1960][df["director_id"] == 46]
print(miyazaki)

"""Q5: 
Create a Pivot Table that shows the median rating for each director, grouped by their respective countries. 
Name your variable 'pivot_agg'
"""

# your code here
pivot_agg = pd.pivot_table(df, index = ["country","director_name"])[["imdb_score"]]
print(pivot_agg)


"""Q6:
How long did the movie Gladiator aim to keep your attention? Save the series with this information
in a variable called 'gladiator_duration', then print it.
"""

# your code here
gladiator_duration = df[df["movie_title"] == "Gladiator"]["duration"]
print(gladiator_duration)
