import sqlite3

from pylab import mpl, plt

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

import pickle
import numpy as np
from random import gauss

a = [gauss(1.5,2) for i in range(100000)]
path = '../SampleData/finance/'
pkl_file = open(path + 'data.pkl', 'wb')
pickle.dump(a, pkl_file)
pkl_file.close()


with open(path + 'data.pkl', 'rb') as pkl_file:
    b = pickle.load(pkl_file)

print(a[:3])
print(b[:3])

np.allclose(np.array(a), np.array(b))

pkl_file = open(path + 'data.pkl', 'wb')
pickle.dump(np.array(a), pkl_file)
pickle.dump(np.array(a)**2, pkl_file)

pkl_file.close()

pkl_file = open(path + 'data.pkl', 'rb')
x = pickle.load(pkl_file)
print(x[:4])
y = pickle.load(pkl_file)
print(y[:4])
pkl_file.close()

pkl_file = open(path + 'data.pkl', 'wb')
pickle.dump({'x':x, 'y':y}, pkl_file)
pkl_file.close()

with open(path + 'data.pkl', 'rb') as pkl_file:
    data = pickle.load(pkl_file)

for key in data.keys():
    print(key, data[key][:4])


import pandas as pd

rows = 5000
a = np.random.standard_normal((rows, 5)).round(4)

print(a)

t = pd.date_range(start='2019/1/1', periods=rows, freq='H')
print(t)


csv_file = open(path + 'data.csv', 'w')
header = 'date,no1,no2,no3,no4,no5\n'
csv_file.write(header)

for t_, (no1, no2, no3, no4, no5) in zip(t,a):
    s = '{},{},{},{},{}\n'.format(t_, no1, no2, no3, no4, no5)
    csv_file.write(s)

csv_file.close()

csv_file = open(path + 'data.csv', 'r')
for i in range(5):
    print(csv_file.readline(), end='')
csv_file.close()

csv_file = open(path + 'data.csv', 'r')
content = csv_file.readline()
print(content[:5])
csv_file.close()

import csv

with open(path + 'data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    lines = [line for line in csv_reader]

print(lines[:5])

import sqlite3 as sp3

con = sqlite3.connect(path + 'numbs.db')
#query = 'CREATE TABLE numbs (Date date, No1 real, No2 read)'
#con.execute(query)
#con.commit()

# q = con.execute
# print(q('SELECT * FROM sqlite_master').fetchall())
#
# import datetime
# now = datetime.datetime.now()
# print(q('INSERT INTO numbs VALUES (?,?,?)', (now, 0.12, 7.3)))
#
# np.random.seed(100)
#
# data = np.random.standard_normal((10000, 2)).round(4)
# for row in data:
#     now = datetime.datetime.now()
#     q('INSERT INTO numbs VALUES (?,?,?)', (now, row[0], row[1]))
#     con.commit()
#
# print(q('SELECT * FROM numbs').fetchmany(4))
#
# print(q('SELECT * FROM numbs WHERE no1 > 0.5').fetchmany(4))
# pointer = q('SELECT * FROM numbs')
#
# for i in range(3):
#     print(pointer.fetchone())
#
# rows = pointer.fetchall()
# print(rows[:3])
#
# print(q('DROP TABLE IF EXISTS numbs'))
# print(q('SELECT * FROM sqlite_master').fetchall())
#
# con.close()

dtimes = np.arange('2019-01-01 10:00:00', '2025-12-31 22:00:00', dtype='datetime64[m]')
print(len(dtimes))

dty = np.dtype([('Date','datetime64[m]'),('No1','f'),('No2','f')])

data['Date'] = dtimes
a = np.random.standard_normal((len(dtimes), 2)).round(4)

data['No1'] = a[:,0]
data['No2'] = a[:,1]



