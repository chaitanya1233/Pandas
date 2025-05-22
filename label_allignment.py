print('Label allignment : means the label is aligned with the text')
import pandas as pd

a = pd.Series([10,20,30],index=['a','b','c'])
b = pd.Series([1,2.3,5],index=['c','a','b'])

c = a+b
print(c)

# if index is not matched --> NaN will be places at the unmatched index
# if index is matched --> the values will be added

# Ex.
x =pd.Series([10,20,40,40],index=['a','b','c','z'])
y = pd.Series([1,2,3],index=['a','z','c'])
z = x+y
print(z)