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

