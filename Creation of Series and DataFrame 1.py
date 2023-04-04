print("Creation of Series and DataFrame part 1")
# series is a data set having same datatype values like integer, string...
# to create series we will import panda
import pandas as pd
data = pd.Series([1,2,3,4,5,6], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(data)

print(data['a'])

# update Values at spacific index
data['a'] = 44
print(data)