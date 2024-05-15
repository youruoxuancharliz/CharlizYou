import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("nba.csv")
# Drop data table down
data

# Print info of data
print( data.info() )

# Return top few and bottom rows
print(data.head(6))
print(data.tail(10))

# return specific columns
data.groupby('Name','Salary')

# return specific columns and rows
data.loc[0,['Name','Salary']]   # row index 0

# sorting values of named columns in order, eg descending
data.sort_values("Salary", ascending=False)

# delete column eg college
data.pop('College') 

# delete row 
newdata = data.drop(data.index[26:]) #===deleting rows 26 onwards, leaving only row index 0-25===

# plotting and SET COLOUR
newdata[['Height', 'Salary']].plot.line(), color={"Height": "red", "Salary": "blue"})


