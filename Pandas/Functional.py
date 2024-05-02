import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(seed=7)
val = np.random.randint(-10,10,size=9).reshape(3,3)
df = pd.DataFrame(val,index=list('def'),columns=list('abc'))
print(df.mean())

print(np.mean(df))

print(df.apply(np.mean))

print(df.apply(np.sum,axis=1))

print(df.apply(lambda x:x+2))

def add(df, n=2):
    return df + n

print(df.apply(add))
print(df.apply(add, n=5))


print(df.apply(np.min))
print(df.agg(np.min))

print(df.agg([np.min]))
print(df.agg([np.min,np.max]))

def max_mean(df):
    return df.max() - df.min()

print(df.agg([max_mean]))

print(df.agg({'a':[np.max,np.min],'b':np.sum}))

def add2(obj):
    return obj+2

print(df.agg([add2]))
print(df.agg([add2,np.abs]))

print(df.applymap(lambda x: True if x > 0 else False))
print(df.applymap(np.sign))

def mapping(val,n=3):
    if val > n:
        return True
    else:
        return False

print(df.applymap(mapping))
print(df.applymap(lambda x: mapping(x, n=4)))

def add(df, p=None):
    return df+p

def div(df,n=None):
    return df/n

def rnd(df,d=None):
    return round(df,d)

print(rnd(div(add(df, p=3),n=3),d=3))

print(df.pipe(add,p=3).pipe(div, n=3).pipe(rnd,d=5))

ser = pd.Series([1,2,3,4,5],index=list('abcde'))
print(ser)

for val in ser:
    print(val)

for idx in ser.index:
    print(idx)

for idx, val in ser.iteritems():
    print(idx, val)

val = [[81,79],[91,90]]
df = pd.DataFrame(val,columns=['math','eng'],index=list('AB'))
print(df)

for col in df:
    print(col)

for col in df.columns:
    print(col)

for idx,val in df.iterrows():
    print(idx)
    print(val, '\n')

df2 = df.copy()
df2['math'] = [81.0,91.0]
print(df2.dtypes)


row = next(df2.iterrows())[1]
print(row)

for idx, value in df2.iterrows():
    df2.loc[idx,'math'] = 'a'

print(df2)

for col, val in df.iteritems():
    print(col)
    print(val,'\n')

for row in df.itertuples():
    print(row)


for row in df.itertuples(index=False):
    print(row)

for row in df.itertuples(name=None):
    print(row)

for col,val in df.iteritems():
    mean = val.mean()
    print(col, 'の平均点は',mean)

for row in df.itertuples():
    print('index:',row[0],'math:',row[1],'eng:',row.eng)


for row in df.itertuples(name=None):
    print(row)

df = pd.read_csv('../SampleData/data/ex15.csv')
print(df)

grouped = df.groupby('sex')
print(grouped)
print(grouped.groups)

print(df.loc[[2,3,6,7],'sex'])
print(grouped.indices)
print(grouped.get_group('Female'))
print(grouped.mean())

print(grouped['math'].mean())
print(grouped[['math','eng']].mean())

grouped = df.groupby(['sex','club'])
print(grouped.mean())


classroom = ['1A']*2 + ['1B']*3 + ['1C']*2 + ['1A']*2
print(classroom)

grouped = df.groupby([classroom, 'sex'])
print(grouped[['math','eng']].max())

df2 = df.copy()
df2 = df2.set_index('club')
print(df2)

print(df2.groupby(level=0).mean())

grouped = df.groupby('sex')
for name,group in grouped:
    print(name)
    print(group[0:2], '\n')

grouped = df.groupby('club')
print(grouped['math'].describe())

print(grouped.filter(lambda x:x['math'].mean() > 80))

set_grouped = df.groupby('sex')
print(set_grouped['math'].nlargest(n=1), '\n')
print(set_grouped['math'].nsmallest(n=1), '\n')

grouped = df.groupby('sex')
print(grouped.agg(np.mean))

print(grouped[['math','eng']].agg([np.max,np.min]))

print(grouped.agg({'math':np.mean,'eng':np.max,'scie':np.min}))

df = pd.read_csv('../SampleData/data/ex16.csv')
print(df)

grouped = df.groupby('category')
print(grouped['sales'].agg(lambda x:x.mean()))
print(grouped['sales'].transform(lambda x:x.mean()))

df2 = df.copy()
df2['カテゴリ平均'] = grouped.transform(lambda x:x.mean())
print(df2)

df2['万'] = grouped.transform(lambda x:x/10000)
print(df2)

df = pd.read_csv('../SampleData/data/ex15.csv')
print(df)

print(df.groupby('sex').apply(lambda x:x.mean()))

def sec(df, col=None):
    temp = (df[col]-df[col].mean())/df[col].std(ddof=0)
    df['score'] = round(50+10*temp)
    df = df[['name','sex','club',col,'score']]
    return df.sort_values(by='score', ascending=False)

df2 = df.copy()
print(sec(df2, col='math'))

df2 = df.copy()
df2.loc[3:5,'math'] = np.nan
df2.loc[[0,6,8],'eng'] = np.nan
df2.loc[[1,7],'scie'] = np.nan
mean = round(df2.mean())
print(mean)

print(df2.fillna(mean))

print(df2.groupby('club').mean())
