import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ser = pd.Series([0,1,2,3,4])
print('最小値',ser.min())
print('最大値',ser.max())

val = np.arange(0,9).reshape(3,3)
df = pd.DataFrame(val,index=list('edf'),columns=list('abc'))
print(df)

print(df.min(axis=0))
print(df.max(axis=1))

print(df.mean(axis=1))

df = pd.DataFrame([[1,3,100,101,102,106,115,110]])
print(df)

print(df.median(axis=1))

df[8] = 120
print(df)
print(df.median(axis=1))

table_a = pd.DataFrame([[152,151,150,147,181,190,187,149,196]])
print(table_a.mean(axis=1))

mean = table_a.mean(axis=1).values[0]
print(mean)

data = table_a.values[0]
print(data)

n = table_a.shape[1]
print(n)

def standard_deviation(data,mean,n):
    std = 0
    for num in data:
        std += (num - mean)**2
        if num == data[n-1]:
            std = (1/n)*std
            std = np.sqrt(std)
            print(std)

standard_deviation(data,mean,n)

print('table_a',table_a.std(axis=1, ddof=0)[0])


df = pd.DataFrame([[1,2,3,4,5,6,7,8,9,10]])
print(df.quantile(q=0.5,axis=1))
print(df.median(axis=1))
print(df.quantile(q=[0.25,0.5,0.75],axis=1))

print(df.quantile(q=0.25,axis=1, interpolation='linear'))
print(df.quantile(q=0.25,axis=1, interpolation='nearest'))
print(df.quantile(q=0.25,axis=1, interpolation='midpoint'))

val = np.arange(0,9).reshape(3,3)
df = pd.DataFrame(val, index=list('def'), columns=list('abc'))
print(df)

print(df.cumsum(axis=0))

df.loc['e','a'] = np.nan
df.loc['f','b'] = np.nan

print(df.cumprod(axis=1))

ser = pd.Series([1,3,5])
print(ser.cumsum())

age = pd.Series([12,14,26,28,30,44,58])
print(age)

print(pd.cut(x=age,bins=[0,10,19,29,39,49,59]))
print(pd.cut(x=age,bins=[0,19,60]))

print(pd.cut(x=age,bins=[0,19,60],labels=['non-adult','adult']))

print(pd.cut(x=age,bins=[0,19,60],right=False))

age_cut =pd.cut(x=age,bins=[0,19,60],labels=['non-adult','adult'])
print(age_cut.value_counts())

age = pd.Series([12,14,26,28,30,44])
print(pd.qcut(x=age,q=2))
print(pd.qcut(x=age,q=4))

print(pd.qcut(x=age,q=2,labels=['younger','older']))

np.random.seed(seed=1)
val = np.random.randint(0,100,size=9).reshape(3,3)
df = pd.DataFrame(val, columns=list('abc'))
print(df.describe())

print(df.describe(percentiles=[0.1,0.2,0.3]))

df['e'] = list('aba')
print(df['e'].describe())

scores = np.random.randint(70,100,size=25).reshape(5,5)
subs = ['math','eng','scie','art','hist']
df = pd.DataFrame(scores,columns=subs)
df['club'] = ['soccer','tennis','tennis','soccer','tennis']
df['sex'] = list('MMFMF')
print(df)

print(pd.pivot_table(df,index='sex',aggfunc=np.mean))
print(pd.pivot_table(df,index='sex',values='art'))
print(pd.pivot_table(df,index='sex',values=['art','eng']))

print(pd.pivot_table(df,index='club',columns='sex',aggfunc=np.mean))

print(pd.pivot_table(df,index=['sex','club'],values='eng',aggfunc=[np.sum,np.min,np.max]))

print(pd.pivot_table(df,index=['sex','club'],aggfunc={'eng':np.min,'math':np.max}))

print(df)

print(pd.pivot_table(df,index='club',values='math',aggfunc=np.mean,margins=True))

sex = np.random.choice(['M','F'],size=10)
eva = np.random.randint(70,100, size=10)
cit = np.random.choice(['Tokyo','Osaka','Sapporo'],size=10)
div = np.random.choice(['sales','hr','marketing','dev'],size=10)
dic = {'sex':sex,'evaluation':eva,'city':cit,'division':div}
df = pd.DataFrame(dic)
print(df)

print(pd.crosstab(index=df['sex'],columns=df['city']))

print(pd.crosstab(index=[df['sex'],df['city']],columns=df['division'],margins=True))

print(pd.crosstab(index=df['sex'],columns=df['city'],values=df['evaluation'],aggfunc=np.mean))

ser = pd.Series([4,5,0,8,3],index=list('abcde'))
print(ser.sort_index())

val = np.random.randint(0,10,size=9).reshape(3,3)
df = pd.DataFrame(val,index=[2,0,1],columns=list('cba'))
print(df)

print(df.sort_index(axis=0))
print(df.sort_index(axis=1))

df.index = [2,np.nan,1]
print(df)

print(df.sort_index(na_position='first'))

print(ser.sort_values())
print(ser.sort_values(ascending=False))


