import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../SampleData/data/ex1.csv')
print(df)

df = pd.read_csv('../SampleData/data/ex1.csv', header=2)
print(df)

df = pd.read_csv('../SampleData/data/ex1.csv', header=None, names=list('アイウエオ'))
print(df)


df = pd.read_csv('../SampleData/data/ex2.csv', index_col='name')
print(df)
df = pd.read_csv('../SampleData/data/ex2.csv', index_col=3)
print(df)

df = pd.read_csv('../SampleData/data/ex2.csv', index_col=['name','sex'])
print(df)


df = pd.read_csv('../SampleData/data/ex2.csv', usecols=['weight'],squeeze=True)
print(df)

df = pd.read_csv('../SampleData/data/ex2.csv', header=None, skiprows=2)
print(df)

df = pd.read_csv('../SampleData/data/ex2.csv', skipfooter=1, engine='python')
print(df)

df = pd.read_csv('../SampleData/data/ex2.csv', nrows=3)
print(df)

df = pd.read_csv('../SampleData/data/ex2.csv', dtype='object')
print(df.info())

df = pd.read_csv('../SampleData/data/ex2.csv')
print(df['stay'].apply(type))

df = pd.read_csv('../SampleData/data/ex2.csv', true_values=['Yes'], false_values=['No'])
print(df['stay'].apply(type))

df = pd.read_csv('../SampleData/data/ex3.csv')
print(df)
print(df['date'].apply(type))

df = pd.read_csv('../SampleData/data/ex3.csv', parse_dates=[['date','time']])
print(df)
print(df['date_time'])


df = pd.read_csv('../SampleData/data/ex4.csv')
print(df)
print(df.isna())

df = pd.read_csv('../SampleData/data/ex4.csv', na_values=['None','?'])
print(df)

df = pd.read_csv('../SampleData/data/ex5.csv', skiprows=[2])
print(df)

df = pd.read_csv('../SampleData/data/ex5.csv', usecols=['a','b','c','d'])
print(df)

df = pd.read_csv('../SampleData/data/ex5.csv', error_bad_lines=False, warn_bad_lines=True)
print(df)

df = pd.read_csv('../SampleData/data/ex6.csv', encoding='UTF-8')
print(df)

df = pd.read_csv('../SampleData/data/ex6.csv', index_col=False)
print(df)

df = pd.read_csv('../SampleData/data/ex7.csv', mangle_dupe_cols=True)
print(df)

df = pd.read_csv('../SampleData/data/ex8.csv', skip_blank_lines=False)
print(df)

df = pd.read_csv('../SampleData/data/ex8.csv', comment='#', skip_blank_lines=True)
print(df)

df = pd.read_csv('../SampleData/data/ex9.csv', sep='|')
print(df)

df = pd.read_csv('../SampleData/data/ex10.csv', sep='\t')
print(df)

df = pd.read_table('../SampleData/data/ex10.csv')
print(df)

df = pd.read_csv('../SampleData/data/ex11.csv', sep='\t')
print(df)
print(df['sales'].apply(type))

df = pd.read_csv('../SampleData/data/ex11.csv', sep='\t', thousands=',')
print(df['sales'].apply(type))

df = pd.DataFrame([[1,2,3],[4,5,6]], columns=list('abc'))
print(df)
df.to_csv('../SampleData/data/out1.csv')

print(pd.read_csv('../SampleData/data/out1.csv'))


df.to_csv('../SampleData/data/out1.csv', index=False)
print(pd.read_csv('../SampleData/data/out1.csv'))

df.to_csv('../SampleData/data/out2.csv', header=False, index=False)
print(pd.read_csv('../SampleData/data/out2.csv'))

print(df.to_csv(index=False, sep='\t'))
print(df.to_csv(index=False, sep='|'))

print(df.to_csv(index=False, columns=['a','c']))

df.index = ['d','e']
print(df)

df.to_csv('../SampleData/data/out3.csv', index=True, index_label='index_label')
print(pd.read_csv('../SampleData/data/out3.csv'))

print(pd.read_excel('../SampleData/data/ex12.xlsx'))

employees = pd.read_excel('../SampleData/data/ex12.xlsx', sheet_name='employees')
print(employees)

div = pd.read_excel('../SampleData/data/ex12.xlsx', sheet_name='div')
print(div)

excel = pd.ExcelFile('../SampleData/data/ex12.xlsx')
print(excel)
print(excel.sheet_names)


val = [['male',22],['female',19]]
df = pd.DataFrame(val,index=['a','b'],columns=['sex','age'])
print(df)

print(df.to_json(orient='columns'))
print(df.to_json(orient='table'))

print(df['age'].to_json(orient='index'))

df.to_json('../SampleData/data/out5.json', orient='columns')

with open('../SampleData/data/out5.json',encoding='UTF-8') as file:
    print(file.read())

df['bdate'] = pd.Timestamp('20190101')
print(df)

print(df.to_json(orient='columns',date_format='iso'))

df2 = df.copy()
df2.loc['a','sex'] = None
df2.loc['b','age'] = np.nan
df2.loc['a','bdate'] = np.nan

print(df2)
print(df2.to_json(orient='columns'))

with open('../SampleData/data/out5.json',encoding='UTF-8') as file:
    print(file.read())

print(pd.read_json('../SampleData/data/out5.json',typ='frame'))

print(pd.read_json('../SampleData/data/ex13.json',typ='series',orient='index'))

df = pd.read_json('../SampleData/data/out5.json',dtype={'age':np.int8})
print(df.info())

df = pd.DataFrame([['あ',1],['い',2]],columns=list('ab'))
print(df)

hdf = pd.HDFStore('../SampleData/data/out7.hdf5')
print(hdf)

print(hdf.put(key='add_df',value=df))

ser = pd.Series([1,3,5,7],index=list('abcd'))
hdf['add_ser'] = ser

df2 = pd.DataFrame([[0.1,2,3],[0.5,4,5]],columns=list('abc'))
df2.to_hdf('../SampleData/data/out7.hdf5',key='add_df2')

print(hdf.get('add_df2'))

df = pd.read_hdf('../SampleData/data/ex14.hdf5', key='out8')
print(df)

df = pd.DataFrame([[0.9,6,7]],columns=list('abc'))
df.to_hdf('../SampleData/data/out9.hdf5',key='add_df', format='table')
print(pd.read_hdf('../SampleData/data/out9.hdf5',key='add_df'))




