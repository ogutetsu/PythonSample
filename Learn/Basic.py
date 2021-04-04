# コメント
"""複数行の
コメント"""

# =================
#  変数
print("変数")

# 文字列
name = "python"
print(name)
type(name)
escape = "python \'3.x"
print(escape)

# 整数
value = 10
value = int(10)
print(value)
type(value)

# 少数
f = 3.14159
f = float(3.14159)
print(f)
type(f)

# 指数
f1 = 1.2e3
print(f1)
f2 = 1.2e-3
print(f2)

# 16進数
h = 0x10
h = int("10", 16)
print(h)

# 8進数
o = 0o10
o = int("10", 8)
print(o)

# 2進数
b = 0b101010
b = int("101010", 2)
print(b)

# リスト
l = [123, 456, 789]
print(l)
# リストの先頭
print(l[0])
# リストの最後尾
print(l[-1])
# リストの要素数
print(len(l))

# タプル リストのイミュータブル版がタプル
t = (123, 456, 789)
print(t)

# リストとタプルの相互変換
l1 = list(t)
print(l1)
t1 = tuple(l)
print(t1)

# オブジェクトのID
print(id(l1))



