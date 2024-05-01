import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame([[1,2],[3,4]], columns=['A','B'])
print(df)


df['C'] = [1,2]
df['D'] = 3
df.loc[:,'E'] = [5,6]
print(df)

df = df.assign(F=[7,8])
print(df)

df.loc[2] = list(range(6))
print(df)

df = pd.DataFrame([[1,2],[3,4]], columns=['A','B'])
print(df)

df2 = pd.DataFrame([[5,6],[7,8]], columns=['A','B'])
print(df2)

print(df.append(df2))

print(df.append(df2,ignore_index=True))

df3 = pd.DataFrame([[7,8,9]], columns=['A','B','C'])
print(df.append(df3))


val = np.arange(0,12).reshape(3,4)
df = pd.DataFrame(val, columns=list('abcd'))
del df['d']
print(df)
print(df.drop(['b'], axis=1))

print(df.drop(labels=2,axis=0))

print(df.drop(columns=['a','c']))

popped = df.pop('c')
print(popped)

df1 = pd.DataFrame({
    'a':['a0','a1','a2'],
    'b':['b0','b1','b2'],
    'c':['c0','c1','c2']
})
print(df1)


df2 = pd.DataFrame({
    'a':['a3','a4','a5'],
    'b':['b3','b4','b5'],
    'c':['c3','c4','c5']
})
print(df2)

print(pd.concat([df1,df2],axis=0))

df3 = pd.DataFrame({
    'a':['a6','a7','a8'],
    'b':['b6','b7','b8'],
    'c':['c6','c7','c8']
})
print(df3)

print(pd.concat([df1,df2,df3],axis=0))

print(pd.concat([df1,df2],axis=1))

dft = df1.copy()
dft.columns = ['a','b','d']
print(pd.concat([df1,dft],axis=0))

dft = df1.copy()
dft.index = [0,2,4]
print(pd.concat([df1,dft],axis=1))

print(pd.concat([df1,dft],axis=1,join='inner'))

print(pd.concat([df1,dft],axis=1).reindex(df1.index))

print(df1.append(df2,ignore_index=True))


ser1 = pd.Series(['s1','s2','s3'])
ser2 = pd.Series(['s4','s5','s6'])
print(ser1.append(ser2))

ser1.index = ['a','b','c']
ser1.name = 'ser1'
print(df1.append(ser1))


leftdf = pd.DataFrame({
    'a':['a0','a1','a2'],
    'b':['b0','b1','b2'],
    'key':['k0','k1','b2']
})
rightdf = pd.DataFrame({
    'c':['c0','c1','c2'],
    'd':['d0','d1','d2'],
    'key':['k0','k1','b2']
})

print(pd.merge(leftdf,rightdf,on='key'))


left2 = leftdf.copy()
left2.columns = ['a','b','key_left']
print(pd.merge(left2,rightdf,left_on='key_left',right_on='key'))

print(pd.merge(leftdf,rightdf,on=['key'],how='inner'))
print(pd.merge(leftdf,rightdf,on=['key'],how='outer'))


left2 = leftdf.copy()
left2.index = left2['key']
left2.drop('key',axis=1,inplace=True)
print(left2)

right2 = rightdf.copy()
right2.index = right2['key']
right2.drop('key',axis=1,inplace=True)
print(right2)

right2 = rightdf[0:2].copy()
right2['key'] = 'k0'
print(right2)

left2 = leftdf[0:2].copy()
left2['key'] = 'k0'
print(left2)

print(pd.merge(left2,right2,on='key'))
#print(pd.merge(left2,right2,on='key',validate='one_to_one'))
print(pd.merge(left2,right2,on='key',validate='many_to_many'))

print(pd.merge(leftdf,rightdf,on='key',suffixes=['_left','_right']))

np.random.seed(seed=1)
val = np.random.randint(0,100,size=16).reshape(4,4)
df = pd.DataFrame(val, index=list('efgh'), columns=list('abcd'))
print(df)

print(df['a'].sample(n=3))
print(df.sample(n=2,axis=0))

print(df.sample(frac=0.3))

print(df.sample(n=1, random_state=1))

print(df.sample(frac=1, axis=0))

print(df.sample(n=3,random_state=5,replace=True))

cities = ['Shibuya','Sapporo','Toyota','Shibuya','Sapporo']
prefs = ['Tokyo','Hokkaido','Aichi','Tokyo','Hokkaido']
df = pd.DataFrame({'city':cities,'pref':prefs})
print(df)

print(pd.get_dummies(df['city']))
print(pd.get_dummies(df['city'],drop_first=True))

print(pd.get_dummies(df))

df['sales'] = [120000,80000,90000,170000,55000]
print(pd.get_dummies(df))

print(pd.get_dummies(df,columns=['city'],prefix='c'))

df['label'] = pd.qcut(df['sales'],3,labels=['low','mid','high'])
print(df)

print(pd.get_dummies(df,columns=['label']))

data = [
    ['A','出身地','Tokyo'],
    ['A','年齢','28'],
    ['A','性別','M'],
    ['B','出身地','Osaka'],
    ['B','年齢','32'],
    ['B','性別','F']
]

df_long = pd.DataFrame(data,columns=['name','attribute','value'])
print(df_long)

print(df_long.pivot(index='name',columns='attribute'))

df_long['flag'] = [1,1,0,0,1,1]
print(df_long.pivot(index='name',columns='attribute',values='flag'))
