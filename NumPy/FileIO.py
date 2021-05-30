import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
np.savetxt('IOFiles/npsample.txt', a)

b = np.loadtxt('IOFiles/npsample.txt')
print(b)

# delimiterを合わせないとエラーになる
np.savetxt('IOFiles/npsample2.txt', a, delimiter=',')
b = np.loadtxt('IOFiles/npsample2.txt', delimiter=',')
print(b)

# 有効桁
np.savetxt('IOFiles/npsample3.txt', a, fmt='%.2e')
np.savetxt('IOFiles/npsample4.txt', a, fmt='%.2f')

# 抜き出す列や行の変更 0,2列目だけを抜き出す
b = np.loadtxt('IOFiles/npsample.txt', usecols=(0, 2))
print(b)

# 0行目をスキップ
b = np.loadtxt('IOFiles/npsample.txt', skiprows=1)
print(b)

# headerとfooterを追加
np.savetxt('IOFiles/npsample5.txt', a, fmt='%.2f', header='this is header', footer='this is footer')

b = np.loadtxt('IOFiles/npsample5.txt')
print(b)

# コメントアウト文字の変更
np.savetxt('IOFiles/npsample6.txt', a, fmt='%.2f', header='this is header', footer='this is footer', comments='>')
b = np.loadtxt('IOFiles/npsample6.txt', comments='>')
print(b)

# データタイプの読み込み
b = np.loadtxt('IOFiles/datatype.csv', dtype=[('col1', 'S20'), ('col2', 'i8'), ('col3', 'f8'), ('col4', 'S10')])
print(b)

name, age, tall, passport = np.loadtxt('IOFiles/datatype.csv',
                                       dtype=[('col1', 'S20'), ('col2', 'i8'), ('col3', 'f8'), ('col4', 'S10')],
                                       unpack=True)
print(name)
print(age)
print(tall)
print(passport)


def passport_cnv(str):
    if str == b'Yes':
        return True
    else:
        return False


b = np.loadtxt('IOFiles/datatype.csv', dtype=[('col1', 'S20'), ('col2', 'i8'), ('col3', 'f8'), ('col4', 'S10')],
               converters={3: lambda s: passport_cnv(s)})
print(b)


# データの欠落に対する挙動を指定する loadtxtの変則版
b = np.genfromtxt('IOFiles/genfrom.txt', delimiter=',')
print(b)

b = np.genfromtxt('IOFiles/genfrom.txt', delimiter=',', dtype=('float', 'float', 'int'))
print(b)


# 配列データをそのまま読み書きする
# 3次元の配列もそのまま読み書きできる
a = np.random.randn(10)
np.save('IOFiles/raw', a)
b = np.load('IOFiles/raw.npy')
print(b)


