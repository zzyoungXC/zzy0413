import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#series代表一列，多列则dataframe
ss=Series(data=list('ABCD'),index=list('abcd'),name='name',dtype=np.str)
#print(ss)
#多个series组成dataframe,df里面数据就是np array
df=DataFrame(data=np.arange(12).reshape(3,4),index=list('abc'),columns=list('xyzw'))
print(df)
print(df.values,type(df.values))
print(df.index)
print(df.columns)

dc=pd.read_csv('groupby.csv')
print('-'*50)
dc.info()
print(dc.head(n=3))
print(type(dc))