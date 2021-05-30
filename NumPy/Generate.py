import numpy as np

# arange
# arange ([start, ]stop, [step, ]dtype = None)
#  start...生成する数列の開始値 省略すると0
#  stop....生成する数列の終点
#  step....生成する数列の間隔値 省略すると1
#  dtype...データ型

a = np.arange(5)
print(a)
a = np.arange(1,5)
print(a)
a = np.arange(1, 10, 2)
print(a)

# linespace　等間隔の数列を生成する
# linespace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#  start...生成する数列の開始値
#  stop....生成する数値の終点
#  num.....等分する値
#  endpoint...stopを要素に含むか
#  retstep....等分した値の差を表示するか
#  dtype...データ型

a = np.linspace(0,2, 3)
print(a)
a = np.linspace(0,2,num=3, endpoint=False)
print(a)
a = np.linspace(0, 2, 3, retstep=True)
print(a)

# eye  単位行列を生成
# eye(N, M=None, k=0, dtype=float, order='C')
#  N....単位行列の行数
#  M....単位行列の列数
#  k....1の要素をどの位置にするか
#  dtype..データ型
#  order..配列の値が行基準(C)で返すか、列基準(F)で返すか

print(np.eye(3))
print(np.eye(3,4))

print(np.eye(3,4,1))

# identity
# identity(n, dtype=float)
#  n...生成する行列のサイズ NxNの正方行列
#  dtype..データ型

print(np.identity(3))


# tile 配列をタイル上に並べる
# tile(A, reps)
#  A...並べたい配列
#  reps...どの軸方向に何回繰り返すかを指定

a = np.arange(3)
print(np.tile(a, 2))

print(np.tile(a, (3,1)))

a = np.arange(6).reshape(2,3)
print(np.tile(a, 2))


# newaxis 配列に新しく次元を追加する
a = np.arange(12).reshape(3,4)
print(a[np.newaxis, :, :])

print(a[:, np.newaxis, :])


