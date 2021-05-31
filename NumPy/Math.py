import numpy as np
import numpy.linalg as LA

a = np.array([1, 2, 3])
b = np.array([2, 4, 6])

# 四則演算
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b))
print(np.mod(a, b))

# 階乗、平方根
print(np.power(a, b))
print(np.sqrt(a))

# 三角関数
print(np.sin(a))
print(np.arcsin(1))

# 角度
print(np.radians(180))
print(np.deg2rad(180))
print(np.rad2deg(3.14))

# 指数、対数
print(np.exp(1))
print(np.log(np.e))

print(np.log2(a))
print(np.log10(a))
print(np.log1p(a))

# 双曲線関数
print(np.sinh(2))
print(np.arcsinh(2))

# 切り捨て、切り上げ、四捨五入
a = np.random.rand(10) * 10
print(a)

print(np.floor(a))
print(np.trunc(a))
print(np.ceil(a))
print(np.round(a))
print(np.around(a))
print(np.rint(a))
print(np.fix(a))

# 複素数
a = 1 + 2j
b = 2 + 1j

# 実部
print(np.real(a))
# 虚部
print(np.imag(a))

print(a + b)

# 共役
print(np.conj(a))

# 絶対値
print(np.absolute(-2))
print(np.abs(-2))
print(np.fabs(-2.5))

# 合計
a = np.arange(10)
print(np.sum(a))
a = np.arange(12).reshape(3,4)
print(np.sum(a, axis=0))
# 次元数をキープ
print(np.sum(a, axis=0, keepdims=True))

# 平均
a = np.random.randint(0, 10, size=10)
print(a)
print(np.average(a))

# 重み付け
w = np.array([0.5, 0.2, 0.1, 0.1, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01])
print(np.average(a, weights=w))

# returned 平均と重さの合計
print(np.average(a, weights=w, returned="True"))

# データ型を指定する
print(np.mean(a, dtype="float32"))

# 中央値
a = np.random.randint(0, 10, size=(3,4))
print(a)
print(np.median(a))

b = a.copy()
# overwrite_input 破壊的操作を行う
print(np.median(b, overwrite_input=True))
print(np.all(a==b))

# 標準偏差
a = np.random.rand(10)
print(a)
print(np.std(a))

# 不偏標準偏差
print(np.std(a, ddof=1))

# 分散
a = np.random.randint(0, 20, size=10)
print(a)
print(np.var(a))
# 不偏分散
print(np.var(a, ddof=1))

# 共分散
print(np.cov(a))
# 標本分散
print(np.cov(a, bias=True))

# 指定された回数分だけ重複してカウント
a = np.random.randint(0,20, size=5)
print(a)
fweights = np.array([2,2,1,1,1])
print(np.cov(a, fweights=fweights))

# 重み
aweights = np.array([2,2,1,1,1])
print(np.cov(a, aweights=aweights))


# 相関関数
a = np.array([
    [1,2,1,4,5,8,10,7],
    [10,2,8,7,9,3,6,5]
])

print(np.corrcoef(a))
b = np.array([4,5,6,3,2,1,8,10])
print(np.corrcoef(a, b))


# 格子列
a = np.array([0,1,2])
b = np.array([3,4,5])

aa, bb = np.meshgrid(a,b)
print(aa)
print(bb)

# 行列の順序
aa, bb= np.meshgrid(a,b, indexing='ij')
print(aa)
print(bb)

# スパースグリッド (メモリを節約できる)
av, bv = np.meshgrid(a, b, sparse=True)
print(av)
print(bv)

# 内積
a = np.array([1, 2])
b = np.array([3, 4])
print(np.dot(a,b))

print(np.dot(np.array([1j, 2j]), np.array([3j, 4j])))

# 行列
a = np.array([[1,2], [3,4]])
b = np.array([[2,1], [6,5]])
print(np.dot(a,b))

# 外積
a = np.array([1, 2, 3])
b = np.array([3, 4, 1])
print(np.cross(a,b))
# 複数の外積
a = np.array([1, 2, 3])
b = np.array([3, 4, 1])
c = np.array([-1,4,-2])
d = np.array([2,1,-1])
ac = np.vstack((a,c))
bd = np.vstack((b,d))
print(np.cross(ac, bd))



# 行列式を求める
a = np.array([[1,2], [4,5]])
print(LA.det(a))

# 固有値と固有ベクトル
a = np.array([[2,0], [0,2]])
print(LA.eig(a))

# 行列のランクを求める
a = np.arange(12).reshape(3,4)
print(LA.matrix_rank(a))

# 逆行列
a = np.arange(4).reshape(2,2)
print(LA.inv(a))
print(np.dot(a, LA.inv(a)))

# 直積
a = np.array([1,2,3,5,6])
b = np.array([3,1,5,3,2,10])
print(np.outer(a,b))

# たたみ込み積分
# https://deepage.net/features/numpy-convolve.html

a = np.array([1,2,3,4,5])
v = np.array([0.1,0.2])

print(np.convolve(a, v, mode='same'))
print(np.convolve(a, v, mode='full'))
print(np.convolve(a, v, mode='valid'))
