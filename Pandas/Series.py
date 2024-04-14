import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

height_list = [185,162,171,155,191,166]
height_series = pd.Series(height_list)
print(height_series)

weight_arr = np.array([72,50,62,88,57])
weight_series = pd.Series(weight_arr)
print(weight_series)

ser = pd.Series([1,2,3],name='some series')
print(ser)

val = [1,2,3,4]
labels = ['apple','banana','cherry','orange']
ser = pd.Series(val,index=labels)
print(ser)
print(ser.index)

print(ser['apple'])
print(ser.iloc[0])
print(ser['apple':'orange'])

print(ser+2)

val = [1,2,3,4,5]
a = pd.Series(val)
b = pd.Series(val, index=[1,2,3,4,5])
c = pd.Series(val, index=list('abcde'))

print(a.index)
print(b.index)
print(c.index)

a = pd.Series([1,2,3])
b = pd.Series([1,1,2])
print(a.is_unique)
print(b.is_unique)

del a[1]
print(a)

ser = pd.Series([1,1,2,2,2,3])
print(ser.drop_duplicates(keep='first'))

ser = pd.Series([1,np.nan,2,np.nan,3],index=list('abcde'))
print(ser.isna())
print(ser[ser.isna()])
print(ser.dropna())


