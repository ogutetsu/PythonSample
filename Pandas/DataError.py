import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame([[0,np.nan,2],[None,4,5]],columns=list('abc'))
print(df.isna())
print(pd.isnull(df))

df2 = df.copy()
df2.loc[1,'a'] = float('inf')
df2.loc[0,'b'] = -np.inf
print(df2)

print(pd.options.mode.use_inf_as_na)
print(df2.isna())

pd.options.mode.use_inf_as_na = True

print(np.nan == np.nan)
print(None == None)

print(df == np.nan)

df['b'] = pd.Timestamp('20190101')
df.iloc[0,1] = np.nan
print(df)

ser = pd.Series([1,2,np.nan,None])
print(ser)


print(df.notna())

print(df[df['a'].isna()])

val = np.arange(0,9).reshape(3,3)
df = pd.DataFrame(val, index=list('def'), columns=list('abc'))
df.loc['d','a'], df.loc['e','b'] = np.nan, np.nan
print(df)

print(df.dropna(axis=0))
print(df.dropna(axis=1))

df2 = df.copy()
df2['a'] = np.nan
print(df2.dropna(axis=1, how='any'))

print(df2.dropna(axis=1,how='all'))

df2.loc['d','b'] = np.nan
df2.loc['d','c'] = np.nan
print(df2)
print(df.dropna(axis=1,thresh=1))

print(df.dropna(axis=1,subset=['d','f']))


val = np.arange(0,9).reshape(3,3)
df = pd.DataFrame(val, index=list('def'), columns=list('abc'))
df.loc['d','a'], df.loc['e','b'] = np.nan, np.nan
print(df.fillna(value=0))

filling = {'a':100,'b':200, 'c':300}
print(df.fillna(value=filling))

print(df.fillna(method='bfill',axis=0))

print(df.fillna(method='bfill',axis=1))

df2 = df.copy()
df2['a'] = np.nan
df2.loc['d','b'] = np.nan
df2.loc['d','c'] = np.nan
print(df2)

print(df2.fillna(method='bfill',axis=0,limit=1))
print(df2.fillna(method='bfill',axis=0,limit=2))


ser = pd.Series([1,2,3],index=['a','b','c'])
print(ser)

print(df.fillna(ser))

print(df.mean())
print(df.fillna(df.mean(), axis=0))
print(df.fillna(df.median(), axis=0))

val = np.arange(0,25).reshape(5,5)
df = pd.DataFrame(val,columns=list('abcde'))

for i, c in enumerate(df.columns):
    df.loc[i,c] = np.nan

print(df)

print(df['b'].interpolate(method='linear'))

df['index'] = df.index
df.plot(kind='scatter', x='index', y='b')
#plt.show()

df2 = df.interpolate(method='linear')
df2.plot(kind='scatter', x='index', y='b')
#plt.show()

height = [178,190,187,179,192,198,188,1.88,178,192,191,184,171]
ser = pd.Series(height)
print(ser)

mean = ser.mean()
std = ser.std(ddof = 0)
print(mean)
print(std)

zscore = (ser-mean)/std
print(zscore)

print(ser[(zscore<-3)|(zscore>3)])

q1 = ser.quantile(0.25)
q3 = ser.quantile(0.75)
iqr = q3-q1
print('q1 = ',q1)
print('q3 = ',q3)
print('IQR = ',iqr)

bottom = q1 - (1.5 * iqr)
up = q3 + (1.5 * iqr)
print(bottom)
print(up)
print(ser[(ser<bottom)|(ser>up)])

val = [100,104,92,98,98,105]
df = pd.DataFrame({'a':val})
df.plot(kind='box')
#plt.show()


val = [[8,7,6],[8,7,6],[8,7,6]]
df = pd.DataFrame(val, index=list('edf'),columns=list('abc'))
print(df)

print(df.duplicated(keep='first'))
print(df.duplicated(keep='last'))


val = [[8,7,6],[8,7,6],[8,5,6]]
df = pd.DataFrame(val, index=list('edf'),columns=list('abc'))
print(df)

print(df.drop_duplicates(keep='first'))
print(df.drop_duplicates(keep='last'))

print(df.drop_duplicates(subset=['a','b'],keep=False))

