import numpy as np

# reshape
# reshape (a, newshape, order)
#  a...変換元の配列
#  newshape...変換後の配列のshape
#  order... モード 'C','F','A'

a = np.arange(12)
print(a)

# 3x4の2次元配列
b = np.reshape(a, (3, 4))

print(b)

# order指定 'C'はデフォルト
c = np.arange(12)
d = np.reshape(c, (3, 4), 'C')
print(d)

# resize
# resize(a, newshape)
# reshapeからorderを省いた物
# reshapeでは、変形後が元の配列と合致しない場合は、エラーになるが
# resizeでは、強制的に実行する
# またresizeは、変換後の要素を共有しない

a = np.arange(12)
b = np.resize(a, (3, 5))
print(b)
c = np.resize(a, (3, 2))
print(c)

# ndarray.resize
# np.resizeと違い、変換後の要素数が違うと例外が発生する

a = np.arange(12)
a.resize((3, 4))
print(a)

# refcheckをFalseにすると配列の形に合わせてくれる
# ただし欠けている部分には0が入る

a.resize((3, 5), refcheck=False)
print(a)

# append
# append(arr, values, axis)
#  arr...要素が追加される配列
#  values...追加する要素または配列
#  axis...どの軸方向に適用するか

a = np.arange(12)
a = np.append(a, [7, 6, 5])
print(a)

b = np.arange(12).reshape(3, 4)
print(b)
b = np.append(b, [[12, 13, 14, 15]], axis=0)
print(b)

# all
# all(a, axis, out, keeddms)
#  a...配列
#  axis...どの軸方向に要素を見ていくか
#  out...結果を格納する配列
#  keepdms...結果の際、要素数が1になった次元もそのまま残すか

a = np.array(
    [
        [1,1,1],
        [1,0,0],
    ]
)

print(np.all(a))

b = np.ones(3)
print(np.all(b))

# aの要素がすべて1以下
print(np.all(a<=1))

# 行方向にみる
print(np.all(a, axis=0))

# keepdmsをTrue
print(np.all(a, axis=0, keepdims=True))

# any
# any(a, axis, out, keepdms)
#  a...配列
#  axis...どの軸方向に要素を見ていくか
#  out...結果を格納する配列
#  keepdms...結果の際、要素数が1になった次元もそのまま残すか

a = np.arange(12).reshape(3,4)
print(np.any(a==1))
print(np.any(a > 5, axis=1))
print(np.any(a > 5, axis=1, keepdims=True))

# where
# where(condition, x, y)
#  condition...条件
#  x, y...conditionがTrueならx Falseならyを返す

a = np.arange(12)

print(np.where(a < 5))

print(a[np.where(a < 5)])

a = np.arange(12).reshape(3, 4)
print(np.where( a % 2 == 0))

print(np.where( a % 2 == 0, "even", "odd"))

print(np.where( a % 2 == 0, (1, 2, 3, 4), (10,11,12,13)))


# max, min
# amax(a, axis, out, keepdims)
#  a...最大値を取得したい配列
#  aixs...最大値を求める軸
#  out...結果を返す配列
#  keepdims...結果の際、要素数が1になった次元もそのまま残すか

a = np.arange(10)
print(np.amax(a))

a = np.arange(12).reshape(3,4)
print(np.amax(a, axis=0))
print(np.amax(a, axis=1))

a = np.random.rand(10)
print(a)
print(a.max())

# nanを最大値として返さない
a[3] = np.NAN
print(a.max())
print(np.nanmax(a))

a = np.arange(10)
print(np.amin(a))


# argmax 配列の最大要素のインデックスを返す
# argmin 配列の最小要素の　〃

# argmax(a, axis, out)
#  a....最大値のインデックスを調べる配列
#  axis...最大値の軸の方向
#  out...結果を返す配列

a = np.random.randint(10, size=10)
print(a)
print(np.argmax(a))

a = np.random.randint(10, size=(3,4))
print(a)
print(np.argmax(a, axis=0))


# transpose 配列の軸を変える(転置行列)
# transpose(axis)
#  axis...転置を行った後の軸の入れ替え方

a = np.arange(12).reshape(3,4)

print(np.transpose(a))

print(a.transpose())

print(a.transpose(1, 0))
print(a.transpose(0, 1))

# Tは引数を指定しないtranspose
print(a.T)


# sort, argsort
#   argsortは、入れ替えられた配列のインデックスを返す
# sort(a, axis, kind, order)
#  a...ソートする配列
#  axis...ソートを行う軸
#  kind...ソートアルゴリズム
#  order...どのフィールドで要素をソートするか

a = np.random.randint(0, 20, size=10)
print(a)
print(np.sort(a))
print(np.argsort(a))

print(np.sort(a, kind='quicksort'))

vals = [('Aaa', 10), ('Bbb', 6), ('Ccc', 8)]
dtype = [('name', 'S10'), ('num', int)]
a = np.array(vals, dtype)
print(np.sort(a, order='num'))

vals = [('Bbb', 10), ('Ccc', 8), ('Aaa', 10)]
a = np.array(vals, dtype)

print(np.sort(a, order=['num', 'name']))

a = np.random.randint(0, 20, size=12).reshape(3, 4)
print(a)
# 軸を指定しない場合は、列方向でソート
print(np.sort(a))
print(np.sort(a, axis=0))

# 配列の中身自体がソートされる
a.sort()
print(a)


# vstack, hstack
# 配列の結合
# vstack(tup)
#  tup...結合したい配列
a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.hstack((a,b))
print(c)

a = np.array([1,2,3]).reshape(-1, 1)
b = np.array([4,5,6]).reshape(-1,1)
print(np.vstack((a,b)))


# 1次元配列に変換 元の配列は変換せずにコピーを返す
a = np.arange(12).reshape(3,4)
b = a.flatten()
print(b)

# 高速で1次元配列に変換
a = np.arange(12).reshape(3,4)
print(a.ravel())

# 行方向に読み取る
print(a.ravel(order='F'))



# frombuffer bytesからndarrayへ高速に変換
# frombuffer(buffer, dtype=float, count=-1, offset=0)
#  buffer...バッファとして読み込むオブジェクト
#  dtype...データ型
#  count...データを読み込む数(-1はすべて)
#  offset...バイト単位で読み込み開始する位置を指定

src = bytes([1,2,3,4,5])
a = np.frombuffer(src, dtype=np.int8)
print(a)


# 要素が0以外のインデックスを取得
a = np.random.randint(0,5,size=10)
print(a)
print(np.nonzero(a))

# whereでも同様のことが可能
print(np.where(a != 0))


# diff  差分を取る
# diff(a, n=1, axis=-1)
#  a...差分を取りたい配列
#  n...差を取りたい微分の階数(差分法)
#  axis...どの軸に差分をとるか

a = np.random.randint(-5,10,size=10)
print(a)
print(np.diff(a, n=1))
print(np.diff(a, n=2))

a = np.random.randint(-5,10,size=(3,4))
print(np.diff(a, axis=0))

# cumsum 足し合わせる
# cumsum(a, axis=None, dtype=None, out=None)
#  a...足し合わせを取りたい配列
#  axis...どの軸に要素を足し合わせるか
#  dtype...返される配列のデータ型
#  out...計算結果の格納先

a = np.random.randint(10, size=10)
print(a)
print(np.cumsum(a))

a = np.random.randint(10, size=(3,4))
print(a)
# 列方向に足す
print(np.cumsum(a, axis=1))


# 配列同士の結合

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.r_[a,b])

# 多次元配列は、axis方向に要素を合わせる
a = np.zeros((1,3))
b = np.ones((2,3))
print(np.r_[a,b])

# スライス表記
print(np.r_[:10])
# 0～9を2刻みで表示
print(np.r_[0:10:2])
# 逆順
print(np.r_[10:0:-1])
# 10等分
print(np.r_[0:9:10j])

# 最後に配列を追加
print(np.r_[0:3, 4, 5])

# 行列
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.r_['r', a, b])
#縦ベクトルにする
print(np.r_['c', a, b])

a = np.zeros((2,3))
b = np.ones((2,2))

print(np.c_[a,b])
