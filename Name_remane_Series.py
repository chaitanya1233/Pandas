# You can name your pandas series.
# Importing the pandas library

import pandas as pd
s2 = pd.Series([1, 2, 3, 4, 5],index = ['a','b','c','d','e'])
print(s2.name)

# Lets assign a name to the series
s2.name = 'Chaitanya Number'
print(s2.name)
# Now lets rename the series 
new_name = "Chaitanya Kale"
s2.rename(new_name, inplace=True)
print