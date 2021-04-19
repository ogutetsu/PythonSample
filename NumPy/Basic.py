import numpy as np

# 配列
na = np.array([1,2,3,4,5])
print(na)
# 2次元配列
na2 = np.array([[1,2,3], [4,5,6]])
print(na2)
# 配列の形状
print(na2.shape)
# 次元数
print(na2.ndim)

# 配列の演算
print(na + 2)
print(na * 2)

# 配列同士の演算
nb = np.array([2, 0, 1, 0, 2])
print(na + nb)
print(na * nb)

# 内積
print(np.dot(na, nb))

# 配列の作成
na = np.arange(10)
print(na)

# (始点、終点、間隔)
na = np.arange(1,20, 2)
print(na)

# (始点、終点、等分)
na = np.linspace(0, 20, 10)
print(na)

# 配列の和
na2 = np.array([[1,2,3], [4,5,6]])
print(np.sum(na2))

# 列ごとの和
print(np.sum(na2, axis=1))

# 配列の形状を変える
print(na2.reshape(3, 2))

na2 = np.array([[1,2,3], [4,5,6]])
# 転置行列
print(na2.T)
print(np.transpose(na2))

# 乱数
print(np.random.rand())
# 乱数　標準正規分布
print(np.random.randn())

# 任意の形状の配列を乱数で初期化
print(np.random.rand(2,3))

# スライシング [始点:終点:間隔]
na = np.array([1,2,3,4,5])
print(na[1:3])

# 配列の反転
print(na[::-1])

# 全範囲
print(na[:])

# メモリアドレス
print(na.data)

# データタイプ
print(na.dtype)

# 情報表示
print(na.flags)

# 1次元配列にした時の要素
print(na2.flat[4])

# 要素数
print(na.size)
print(na.itemsize)

# バイトオーダーでの配列の長さ
print(na.nbytes)

# na.size * na.itemsize == na.nbytesになる


# 複素数
c = np.array([1.-2.3j, 2.3+4.j, 3.-3.2j])

# 実部
print(c.real)

# 虚部
print(c.imag)

# 各次元方向に1つ要素を移動するためのバイトオーダー
print(na2.strides)

# ctypesを使ったモジュール操作
print(na.ctypes.data)


# ベースとなる配列
nac = na[:2]
print(nac.base)

print(nac.base is na)   # True
print(nac.base is na.base)  # False


na = np.random.randn(100,100)
# Row
nb = np.array(na, order='C')
# Column
nc = np.array(na, order='F')

print(nb.strides)
print(nc.strides)

# 配列の要素がすべて一致しているか
print(np.allclose(nb,nc))

# すべての要素を1で初期化
ni = np.ones((10,))
print(ni)

# 1000個飛ばしで読みこむ
ni2 = np.ones((10000,))[::1000]
print(ni2)

# 何度も計算する必要がある場合は、copyする
ni2_copy = np.copy(ni2)
print(ni2_copy.sum())


# ブロードキャスト
print(np.array([[1,2,3]]) + [1])

# 次元の違う配列同士の演算
na = np.array([[1,2]])
nb = np.array([3,4])
print(na.shape)
print(nb.shape)
print(na + nb)

na = np.array([[1,2]])
nb = np.array([[3,4], [5,6]])
print(na + nb)

# 5x5の2次元配列
na = np.arange(25).reshape(5,5)
print(na)

# 1～2行目、3～4列目を抜き出す
print(na[1:3, 2:4])
# 行の方向に1つ飛ばしで抜き出す
print(na[::2, :])
# 逆順
print(na[::-1, ::-1])

# データタイプを指定して配列を作成

i32 = np.array([0,1,2], dtype='int32')
print(i32.dtype)
f = np.array([0,1,2], dtype='float32')
print(f.dtype)
i64 = np.array([0,1,2],dtype='int64')
print(i64.dtype)
b = np.array([0, 1, 2], dtype='bool')
print(b)
i8 = np.array([0,1,2], dtype='int8')
print(i8.dtype)


# copy view
# view 元の配列と同じメモリを参照している
na = np.array([1,2,3])
nb = na.view()
nb[0] = 0
print(na)
print(nb)
print(nb.base)

# copy 完全に別の配列
nc = na.copy()
nc[0] = 10
print(na)
print(nc)
print(nc.base)

# 違うオブジェクトの参照
# NumPyではViewになる
nc = na[:]
print(id(na) == id(nc))
nc[0] = 100
print(na)

# 演算による違い
na = np.array([1,2,3])
nc = na
na = na + 1
print(nc)
na = np.array([1,2,3])
nc = na
na += 1
print(nc)

# ViewかCopyか調べる
na = np.array([1,2,3])
nb = na.view()
nc = na.copy()

print(np.may_share_memory(na,nb))
print(np.may_share_memory(na,nc))

# より厳密な判定
print(np.shares_memory(na,nb))
print(np.shares_memory(na,nc))


