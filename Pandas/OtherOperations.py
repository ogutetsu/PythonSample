import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'city':['Tokyo','osaka',np.nan,'TOKYO'],
    'job':[np.nan,'Engineer','teacher','Teacher'],
}, index=['Taro','jiro',np.nan,'Ichiro ']
)

print(df)

print(df['city'].str.lower())

print(df['city'].str.upper())

print(df['city'].str.len())

print(df.index.str.len())

print(df.index.str.strip())
print(df.index.str.strip().str.len())

print(df.index.str.capitalize())

ser = pd.Series(['A + B + C','D + E','F'])
print(ser)

print(ser.str.split(pat='+'))
print(ser.str.split(pat='+', expand=True))

ser = pd.Series(['A + B - C','D * E','F'])
print(ser)

print(ser.str.split(pat='\W', expand=True))

ser = pd.Series(['aBCd','AbCd'])
print(ser)

print(ser.str.replace('a',repl=''))

print(ser.str.replace('a',repl='', case=False))

df = pd.DataFrame(
    [
        'Tokyo 2019-01-02 0 158.3',
        'Osaka 2018-12-02 0 161.7',
        'Tokyo 2019-02-22 0 169.9',
        'Sapporo 2019-01-01 1 179.2',
        'Osaka 2018-11-29 180.2'
    ],columns=['data']
    )

print(df)

df['date'] = df['data'].str.extract('(....-..-..)',expand=True)
print(df)

df['sex'] = df['data'].str.extract('(\d)', expand=True)
print(df)

df['height'] = df['data'].str.extract('(\d\d\d\.\d)', expand=True)
df['location'] = df['data'].str.extract('([A-Z]\w{0,})', expand=True)
print(df)

df = pd.DataFrame({
    'name':['Matsuda','Fuji',np.nan,'maruyama'],
    'div':['sales','HR','hr',np.nan]
})
print(df)
print(df['div'].str.contains('HR',case=True))

print(df['div'].str.contains('sales|hr',case=False,na=False))
cond = df['div'].str.contains('sales|hr',case=False,na=False)
print(df[cond])

print(df['div'].str.endswith(pat='r'))
print(df['div'].str.endswith(pat='M'))

ser = pd.Series([
    'blue.red,blue,yellow',
    'red,yellow',
    'green,blue,red',
    'yellow,green,red',
])

print(ser)

print(ser.str.get_dummies(sep=','))
ser[4] = np.nan
print(ser.str.get_dummies(sep=','))

np.random.seed(0)
val = np.random.randint(-5,5,size=500).reshape(100,5)
df = pd.DataFrame(val, columns=list('abcde')).cumsum()
print(df.head(3))

df['a'].plot(kind='line')
#plt.show()
df.plot(kind='line')
#plt.show()

df['c'].plot(grid=True,xlim=(0,20),ylim=(-30,30))
#plt.show()

df[['a','b']].plot(subplots=True)
#plt.show()

df.iloc[1,:].plot(kind='bar')
#plt.show()
df.iloc[0:10,:].plot(kind='bar')
#plt.show()

df.iloc[0:3,:].plot(kind='barh')
#plt.show()

usecols = ['age','workclass','education','education.num','marital.status','race','hours.per.week']
adult = pd.read_csv('../SampleData/data/adult.csv',usecols=usecols)
print(adult.head(3))

adult['age'].plot(kind='hist',bins=10)
#plt.show()

adult['age'].plot(kind='hist',bins=73,xticks=np.arange(17,90,3),grid=True)
#plt.show()

adult.sample(500,random_state=0).plot(kind='scatter',x='age',y='hours.per.week')
#plt.show()

sub = adult.sample(100, random_state=0)
ax = sub.plot(kind='scatter',x='age',y='education.num',color='r')
sub.plot(kind='scatter',x='age',y='hours.per.week',color='g',ax=ax)
#plt.show()

plt.clf()
np.random.seed(0)
val = np.random.randint(0,5,size=500).reshape(100,5)
df = pd.DataFrame(val,columns=list('abcde')).cumsum()
df.iloc[20:30,0] = np.nan
df['a'].plot(kind='line')
#plt.show()

plt.clf()
df['a'][10:40].plot(kind='bar')
#plt.show()

name=['A','B','C','D','E','F','G']
address = ['Tokyo','Tokyo','Tokyo','Tokyo','Osaka','Osaka','Sapporo']
sex =['F','F','F','M','M','M','M']
div=['HR','Sales','Marketing','Sales','HR','Marketing','Marketing']
age=[25,31,32,28,29,39,38]
point=[88,91,79,89,85,98,82]
df = pd.DataFrame({
    'name':name,
    'address':address,
    'sex':sex,
    'div':div,
    'age':age,
    'point':point
})
print(df)

tuples = list(zip(address,sex))
print(tuples)

midx = pd.MultiIndex.from_tuples(tuples)
print(midx)

print(midx.levels)

midx = pd.MultiIndex.from_tuples(tuples,names = ['address','sex'])
print(midx.names)

ser = pd.Series(age,index=midx)
print(ser.index)
print(ser)

print(pd.Series(age,index=[address,sex]))

np.random.seed(0)
temp1 = ['Tokyo','Osaka','Sapporo']
temp2 = ['F','M']
midx2 = pd.MultiIndex.from_product([temp1,temp2],names=['address','sex'])
ser = pd.Series(np.random.randint(10,size=6),index=midx2)
print(ser)

df = pd.DataFrame({'age':age,'point':point}, index=midx)
print(df)
print(df.T)
print(df.index.nlevels)

print(df.index.get_level_values('address'))
print(df.index.get_level_values(0))
print(df.index.get_level_values(1))

print(df.sort_index(axis=0,ascending=True))
print(df.sort_index(axis=0,level=1, sort_remaining=True))
print(df.sort_index(level=['address','sex'],sort_remaining=False))

#print(df.loc['Tokyo','F'])

print(df.sort_index(level=['address','sex']).loc['Tokyo','F'])

print(df.sort_index(level=0).loc['Osaka':'Sapporo'])


df_col = df.T.copy()
print(df_col)
print(df_col['Tokyo'])

print(df_col['Tokyo']['M'])

df.sort_index(level=0,inplace=True)
print(df.loc['Osaka':'Sapporo'])

print(df.xs(key='Tokyo'))

df2 = df.copy()
df2.index = df2.index.set_levels(
    levels=[['女','男']],
    level=['sex']
)
print(df2)

print(df2.index.levels[0])

df2.index = df2.index.set_codes(codes=[1,1,1,0,0,2,2],level=0)
print(df2)

print(df2.swaplevel(i='sex',j='address'))

df2 = df2.reset_index()
print(df2)

print(df2.set_index(['address','sex']))

print(df.mean(axis=0))
print(df.mean(axis=1))

print(df['age'].mean(axis=0,level='address'))
print(df['age'].mean(axis=0,level=['address','sex']))

grouped = df.groupby(level='sex')
print(grouped.mean())

print(df.groupby(by=['sex','age']).min())

grouper = pd.Grouper(level=1)
print(df.groupby(by=[grouper,'age']).min())

val = {'A':['a0','a1','a2'],'B':['b0','b1','b2']}
idx = pd.Index(['s0','s1','s2'],name='1st')
single = pd.DataFrame(val, index=idx)
print(single)

val_idx = [['s0','s1','s2','s3'],['m0','m1','m2','m3']]
midx = pd.MultiIndex.from_arrays(val_idx, names=['1st','2nd'])
val_df = {'C':['c0','c1','c2','c3'],'D':['d0','d1','d2','d3']}
multi = pd.DataFrame(val_df, index=midx)
print(multi)

print(single.join(multi,how='outer'))

import datetime

dt = datetime.datetime(year=2019,month=5,day=1,hour=10,minute=0,second=15)
print(dt)

dtt = datetime.datetime.today()
print(dtt)

print(dt.date())

delta = dt-datetime.datetime(2019,5,15,19,0,0)
print(delta)

delta = datetime.timedelta(days=1, hours=10)
print(dt)
print(dt+delta)

ts = pd.Timestamp(datetime.datetime(2019,4,1,15,20,45,900))
print(ts)

print(ts.replace(year=2020))

days = [datetime.datetime(2019,1,1), datetime.datetime(2019,1,1),datetime.datetime(2019,1,2),None]
didx = pd.DataFrame(days)
print(didx)

print(pd.Index(['2019-01-01','2019-01-02']))
print(pd.Index(days))

print(pd.date_range(start='20190101',periods=5,freq='W-SUN'))

sidx = pd.Series(days)
print(pd.Series(np.arange(len(sidx)),index=sidx))

p = pd.Period('20190101',freq='D')
print(p)

p = pd.Period('2019-02',freq='M')
print(p)
print(p.start_time)
print(p.end_time)

p = pd.Period('20190405 11:00', freq='H')
print(p)
print(p + datetime.timedelta(hours=5))
print(p + datetime.timedelta(hours=-2))

timestamps = [pd.Timestamp('20190401'),pd.Timestamp('20190402')]
print(pd.Index(timestamps))

periods = [pd.Period('201904',freq='M'),pd.Period('201905',freq='M')]
print(pd.Index(periods))

years = ['2017','2018','2019']
pidx = pd.PeriodIndex(years,freq='A-DEC')
print(pidx)
print(pidx.asfreq('D'))

print(pd.date_range(start='20110501',periods=2,freq='AS-JAN'))


rng = pd.date_range('20181229','20190102',freq='D')
np.random.seed(seed=42)
ser = pd.Series(np.random.randint(0,10,len(rng)),index=rng)
print(ser)
print(ser.shift(2))
print(ser.shift(-2,freq='D'))

diff = ser-ser.shift(1)
print(diff)

idx = pd.date_range('20190101', periods=2, freq='W-SUN')
ser = pd.Series([1,2],index=idx)
print(ser)

print(ser.asfreq(freq='D'))
print(ser.asfreq(freq='2D',fill_value=0))
print(ser.asfreq(freq='B',method='ffill'))

rng = index = pd.date_range(start='20190415',periods=7,freq='D')
ser = pd.Series(np.arange(7),index=rng)
print(ser)

resampled = ser.resample(rule='3D')
print(resampled)
print(resampled.mean())
print(resampled.ohlc())

rng = pd.date_range('20190101 00:00',periods=5,freq='h')
val = np.arange(len(rng)*3).reshape(len(rng),3)
df = pd.DataFrame(val,index=rng,columns=list('abc'))
print(df)

print(df.resample('3H').sum())

df['d'] = df.index
df.reset_index(drop=True,inplace=True)
print(df)

print(df.resample(rule='2H',on='d').mean())




