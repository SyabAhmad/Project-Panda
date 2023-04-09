# Project-Panda

### There are two type Dataframes

```Series``` and ```DataFrames```

```Series``` are ```1D``` labeled ```homogeneously-typed``` array and 

```Dataframes``` are General ```2D``` labeled, size-mutable tabular structure with potentially ```heterogeneously-typed``` column

### Creation od series and Data Frames

### to import Panda 

```python runable
import pandas as pd

```

### To create Series

```python runable
import pandas as pd
# will create a series of data
data = pd.Series([1,2,3,4,5,6,7,8])
# will print the data
print(data)

```

### to print type of data

```python runable
# will print the type of data objects
print(type(data))

```
### To create Dataframe

```python runable
import pandas as pd
# will create a series of data
data = pd.Dataframe(["Column1": [1,2,3,4,5,6], "Column2": [1,2,3,4,5,6]], index=['a','b', 'c', 'd', 'e', 'f'])
# will print the data
print(data)

```

### to print type of data

```python runable
# will print the type of data objects
print(type(data))

```

### to create Seriese from day 1 and day 2 only
```python runable
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
```


