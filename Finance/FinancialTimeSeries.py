import numpy as np
import pandas as pd
from pylab import mpl, plt

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

filename = '../SampleData/finance/tr_eikon_eod_data.csv'

f = open(filename,'r')
print(f.readline()[:5])

data = pd.read_csv(filename,index_col=0,parse_dates=True)
print(data.info())

print(data.head())

#data.plot(figsize=(10,12), subplots=True)
#plt.show()

instruments = ['Apple','Microsoft','Intel','Amazon', 'GoldmanSachs', 'S&P 500 ETF', 'S&P 500 Index', 'VIX', 'EUR/USD', 'Gold', 'Gold Miners ETF', 'SPDR Gold']

for ric, name in zip(data.columns,instruments):
    print('{:8s} | {}'.format(ric,name))

print(data.describe().round(2))
print(data.mean())

print(data.diff().head())

print(data.pct_change().round(3).head())

#data.pct_change().mean().plot(kind='bar', figsize=(10,6))
#plt.show()


rets = np.log(data /data.shift(1))
print(rets.round(3))

#rets.cumsum().apply(np.exp).plot()
#plt.show()

print(data.resample('1w', label='right').last().head())

#rets.cumsum().apply(np.exp).resample('1m', label='right').last().plot()
#plt.show()

sym = 'AAPL.O'
data = pd.DataFrame(data[sym]).dropna()
print(data.tail())

window = 20
data['min'] = data[sym].rolling(window).min()
data['max'] = data[sym].rolling(window).max()
data['mean'] = data[sym].rolling(window).mean()
data['std'] = data[sym].rolling(window).std()
data['median'] = data[sym].rolling(window).median()
data['ewma'] = data[sym].ewm(halflife=0.5,min_periods=window).mean()
print(data.dropna().head())

ax = data[['min','mean','max']].iloc[-200:].plot(
    figsize=(10,6), style=['g--','r--','g--'], lw=0.8)
data[sym].iloc[-200:].plot(ax=ax, lw=2.0)
#plt.show()

plt.clf()

data['SMA1'] = data[sym].rolling(window=42).mean()
data['SMA2'] = data[sym].rolling(window=252).mean()
print(data[[sym, 'SMA1', 'SMA2']].tail())

data[[sym, 'SMA1', 'SMA2']].plot()
#plt.show()
plt.clf()

data.dropna(inplace=True)

data['positions'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
ax = data[[sym, 'SMA1', 'SMA2', 'positions']].plot(figsize=(10,6), secondary_y='positions')
ax.get_legend().set_bbox_to_anchor((0.25,0.85))

#plt.show()

plt.clf()

raw = pd.read_csv('../SampleData/finance/tr_eikon_eod_data.csv', index_col=0, parse_dates=True)
data = raw[['.SPX','.VIX']].dropna()

print(data.tail())

data.plot(subplots=True, figsize=(10,6))
#plt.show()

plt.clf()

data.loc[:'2012-12-31'].plot(secondary_y = '.VIX', figsize=(10,6))
#plt.show()
plt.clf()

rets = np.log(data/data.shift(1))
print(rets.head())

rets.dropna(inplace=True)
rets.plot(subplots=True, figsize=(10,6))
#plt.show()
plt.clf()

pd.plotting.scatter_matrix(
    rets,
    alpha = 0.2,
    diagonal='hist',
    hist_kwds={'bins':35},
    figsize=(10,6)
)
#plt.show()
plt.clf()

reg = np.polyfit(rets['.SPX'], rets['.VIX'], deg=1)
ax = rets.plot(kind='scatter', x='.SPX', y='.VIX', figsize=(10,6))
ax.plot(rets['.SPX'], np.polyval(reg,rets['.SPX']), 'r', lw=2)
#plt.show()
plt.clf()


rets.corr()
ax = rets['.SPX'].rolling(window=252).corr(rets['.VIX']).plot()
ax.axhline(rets.corr().iloc[0,1], c='r')
#plt.show()
plt.clf()

tick = pd.read_csv('../SampleData/finance/fxcm_eur_usd_tick_data.csv',index_col=0,parse_dates=True)
print(tick.info())

tick['Mid'] = tick.mean(axis=1)
tick['Mid'].plot(figsize=(10,6))
#plt.show()
plt.clf()

tick_resm = tick.resample(rule='5min', label='right').last()
print(tick_resm.head())
tick_resm['Mid'].plot()
#plt.show()
plt.clf()

