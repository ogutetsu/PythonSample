import pandas as pd
import numpy as np


df = pd.DataFrame([[1,2,3],[4,5,6]])
print(df)

print(df.index)
print(df.columns)

idx = pd.Index([1,2,3,4,5])
print(idx)

print(idx[0])
print(idx[1:3])

ser_obj = {1,1,2,2,4,5}
idx3 = pd.Index([1,1,2,2,4,5])
print(ser_obj)
print(idx3)

idx = pd.RangeIndex(start=0, stop=5, step=1)
print(idx)

idx_date = pd.DatetimeIndex(
    ['2018-12-28','2019-01-05']
)

print(idx_date)

idx_arr = pd.Index([1,2,3])
print(type(idx_arr))
print(type(idx_arr.values))

val = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(val,index=[0,2,4],columns=list('abc'))
print(df)

print(df.reindex([0,1,2,3,4]))

print(df.reindex(columns=list('abcd')))
print(df.reindex([5,6,7,8,9,10], method='ffill'))

idx = pd.Index([5,1,3,4,2])
print(idx)
print(idx.sort_values())














