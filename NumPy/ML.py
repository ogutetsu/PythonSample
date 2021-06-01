import numpy as np

# 機械学習関連

# z-score

def zscore(x, axis=None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd = np.std(x, axis=axis, keepdims=True)
    zscore = (x-xmean)/xstd
    return zscore

a = np.random.randint(10, size=(2,5))
print(a)
print(zscore(a))

b = zscore(a, axis=1)
print(b.std(axis=1))


# min-max
def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)
    return result

print(min_max(a))


# normalize
def normalize(v, axis=-1, order=2):
    l2 = np.linalg.norm(v, ord=order, axis=axis, keepdims=True)
    l2[l2==0] = 1
    return v/l2

print(normalize(a))
print(normalize(a, axis=None))


