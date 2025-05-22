print('Vectorized operations and label alignment with Series')
# Import the pandas libery
import pandas as pd
# Create a series object
s = pd.Series([10,20,30],index = ['a','b','c'])
# Print the series object
print(s)

# Perform vectorized operations
print(s*3)
# s*3 --> This will multiply each elemnt of the series by 3

print(s+5)
# s+5 --> This will add 5 to each element of the series

# Series objetct is immutable