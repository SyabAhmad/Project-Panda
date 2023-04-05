import pandas as pd
import matplotlib.pyplot as plt
# we will use same csv file
# customerdata = pd.read_csv('customers-100.csv', index_col= 0, parse_dates=True)
customerdata = pd.read_excel('population.xlsx', index_col= 0, parse_dates=True)
print(customerdata)

#customerdata = customerdata[["Phone 1", "Phone 2"]].head(5)


# customerdata.plot()
# plt.show()