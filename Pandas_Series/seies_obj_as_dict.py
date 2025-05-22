#  Series object as dictionary
# 1. Import pandas library
import pandas as pd
# 2. Create a Series object
s = pd.Series([1, 2, 3, 4, 5])
# 3. Convert Series object to dictionary
s_dict = s.to_dict()
# 4. Print the dictionary
print(s_dict)
# 5. Print the type of the dictionary
print(type(s_dict))
# 6. Print the Series object
print(s)
# 7. Print the type of the Series object
print(type(s))
# 8. Print the index of the Series object
print(s.index)
# 9. Print the values of the Series object
print(s.values)
# 10. Print the index of the dictionary
print(s_dict.keys())
# 11. Print the values of the dictionary
print(s_dict.values())
# 12. Print the index of the Series object as a list
print(s.index.tolist())
# 13. Print the values of the Series object as a list
list_values = s.tolist()
print("Print the list values:",list_values)