import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

val = ['a', 1, 0.5]
df = pd.DataFrame(val)
print(df)

val = [[1,2,3],[4,5,6]]
df = pd.DataFrame(val, index=['a','b'], columns=['c','d','e'])
print(df)

dic = {'a':[1,2,3], 'b':[4,5,6]}
df = pd.DataFrame(dic)
print(df)

age = pd.Series([10,12,9],index=list('ABC'))
sex = pd.Series(['M','F','M'],index=['C','A','D'])
df = pd.DataFrame({'age':age, 'sex':sex})
print(df)

df = pd.DataFrame(
    {
        'math':[82,93,77],
        'eng':[77,87,71],
        'chem':[69,90,88]
    })
print(df)
print(df['math'])
print(type(df['math']))

print(df[['math','eng']])

print(df.index)

print(df.shape)

df.iloc[1,1] = 100
print(df)

df['new1'] = 10
print(df)

val = [[1,2,3],[4,5,6],[1,2,3],[3,5,6],[1,2,3]]
df = pd.DataFrame(val, columns=list('ABC'))
print(df)
print(df.duplicated(keep='first'))
print(df[df.duplicated(keep='first')])

val = [[1,2,3],[4,5,np.nan],[1,np.nan,np.nan],[3,5,6],[7,8,9]]
df = pd.DataFrame(val, columns=list('ABC'))
print(df.isna())

print(df.dropna(axis=1))


