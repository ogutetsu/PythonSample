import numpy as np

# 1つの乱数を返す
print(np.random.rand())

# 正規分布
print(np.random.normal())

# 0～9の範囲
print(np.random.randint(10))

# 3x4の行列
print(np.random.rand(3,4))

# 0～9の範囲で 3x4の行列
print(np.random.randint(10, size=(3,4)))

# 5～9の範囲
print(np.random.randint(5, 10, size=5))

# シード
np.random.seed(seed=10)
print(np.random.rand())
np.random.seed(seed=10)
print(np.random.rand())

a = np.arange(10)
# aから2つの要素をランダムに取り出す
print(np.random.choice(a, 2))

a = np.random.randint(10, size=10)
print(a)
print(np.random.choice(a, 4, replace=False))

# 重み付け
b = np.random.choice(a, 10, p = [0.5, 0.4, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
print(b)

# シャッフル

a = np.arange(10)
np.random.shuffle(a)
print(a)

# 正規分布
a = np.random.normal(loc=1, scale=1.0, size=10)
print(a)

# 二項分布
#  (n,p)での事象が起こる回数
a = np.random.binomial(n=100, p=0.5, size=10)
print(a)

# ベータ分布
a = np.random.beta(a=1, b=2, size=10)
print(a)

# ガンマ分布
a = np.random.gamma(shape=2, scale=2, size=10)
print(a)

# ポアソン分布
a = np.random.poisson(lam=10, size=10)
print(a)

# カイ二乗分布
a = np.random.chisquare(df=2, size=10)
print(a)