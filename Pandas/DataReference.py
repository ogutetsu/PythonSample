import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


val = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(val, index=[1,2,3],columns=list('def'))
print(df)

# インデックスラベル2
print(df.loc[2])

# 位置インデックス2
print(df.iloc[2])

val = np.arange(1,10).reshape(3,3)
df = pd.DataFrame(val, index=[1,2,3],columns=list('def'))
print(df)

print(df['e'])
print(df[['e','d']])

df2 = pd.DataFrame(val,index=[0,5,10],columns=[1,2,3])
print(df2)

# 行の選択
print(df2[0:2])


val = np.arange(0,25).reshape(5,5)
df = pd.DataFrame(val,index=[10,5,2,12,6],columns=list('abcde'))
print(df)

# 2から4までの行列を選択
print(df[2:4])

# 始点0,終点5,公差2の行を選択
print(df[0:5:2])

#逆順で選択
print(df[::-1])

# 属性参照
ser = pd.Series([1,2,3],index=list('abc'))
print(ser.a)
print(df.d)

# bool配列参照
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(df[[True,False,True]])


np.random.seed(seed=1)
val = np.random.randint(0,10,size=25).reshape(5,5)
print(val)

df = pd.DataFrame(val,columns=list('abcde'))
print(df)

print(df['a'] > 3)

print(df[df['a'] > 3])

# seriesのwhere
ser = pd.Series([1,2,3,4,5])

# 3より大きいものを抽出
print(ser[ser > 3])
print(ser.where(ser > 3))

# dataframeのwhere
print(df[df > 3])
print(df.where(df > 3))

# 0を-1へ変換
df = df.where(~(df == 0), other=-1)
print(df)

df[df == -1] = 0
print(df)






