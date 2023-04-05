import pandas as pd
import numpy as np
print("Playing with Tabular Data")
customerData = pd.read_csv('customers-100.csv')
customerData = pd.DataFrame(customerData)

# to print Data
print(customerData)
# to print specific Column
print(customerData["Customer Id"])

# to print first rows to the count value
print(customerData.head(10))

# to print last rows to the count value
print(customerData.tail(5))
# to print total count
print(customerData.count())

# to print total count of single column
print(customerData["Customer Id"].count())

# to print columns Names
print(customerData.columns)

# to find technical info about that Data e.g.g size of document, Data Types
print(customerData.info())


