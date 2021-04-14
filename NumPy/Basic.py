import numpy as np

# 配列
na = np.array([1,2,3,4,5])
print(na)
# 2次元配列
na2 = np.array([[1,2,3], [4,5,6]])
print(na2)
# 配列の形状
print(na2.shape)

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

