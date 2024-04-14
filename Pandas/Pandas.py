import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '../SampleData/'
file = 'adult.data'
df = pd.read_csv(path + file, header=None, skipinitialspace=True, na_values="?")

print(df.iloc[0:2])

col_name = ['age','workclass','fnlwgt','education','education.num','marital.status','occupation','relationship','race','sex','capital.gain','capital.loss','hours.per.week','native.country','income']
df.columns = col_name
print(df.iloc[25:28])

df = df.drop(columns=['fnlwgt','relationship','race','capital.gain','capital.loss','native.country'])
print(df.columns)

print(df.head())
print(df.tail())
print(df.info())

print(df['age'].describe())

print(df[['education','workclass']].describe())

print(df['education'].value_counts())


print(df.loc[0:2,['education','workclass']])

print(df.iloc[100:103,:])

print(df[df['sex'] == 'Male'].shape)
print(df[df['sex'] == 'Female'].shape)

print(df[df['sex'] == 'Male']['age'].describe())
print(df[df['sex'] == 'Female']['age'].describe())

print(df.sort_values(by='age').head(3))

print(df.sort_values(by=['age','education.num']).head(3))


print(df.isna().any(axis=0))

print(df.isna().sum(axis=0))

df.dropna(inplace=True)
print(df.isna().sum(axis=0))


grouped = df.groupby('sex')
print(grouped.mean())

grouped = df.groupby('workclass')
print(grouped['hours.per.week'].mean())

grouped = df.groupby(['age','workclass'])
print(grouped['hours.per.week'].mean())

grouped = df.groupby('workclass')
workclass_hours = pd.DataFrame(grouped['hours.per.week'].mean())
print(workclass_hours)


merged = df.merge(workclass_hours,
                  left_on='workclass',
                  right_index=True,
                  suffixes=('','_avg'))

print(merged[['workclass','hours.per.week','hours.per.week_avg']].head())


merged['marital.status'].value_counts().plot(kind='bar')
plt.show()
