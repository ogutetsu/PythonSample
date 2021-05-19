import numpy as np

# 0で初期化
a = np.zeros(10, dtype=int)
print(a)

a = np.zeros((3,4))
print(a)

# 0で初期化する必要がない場合
# 値が0かどうかは保証されない
a = np.empty(10)
print(a)

# 同じ要素の配列を作成して0でクリアする
a = np.arange(12).reshape(3, 4)
b = np.zeros_like(a)
print(b)

# 1で初期化
a = np.ones(10, dtype=int)
print(a)

a = np.arange(12).reshape(3, 4)
b = np.ones_like(a)
print(b)

