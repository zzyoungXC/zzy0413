import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dc=pd.read_csv('groupby.csv')
print('-'*50)
dc.info()
print('---->',dc.head(n=3))
print(type(dc))