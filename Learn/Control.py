# if文
val = 20
if val >= 10:
    print("10より大きい")

v1 = 10
v2 = v1
print(v1, v2)
if v1 == v2: print("v1とv2は同じ")

v2 = 20
print(v1, v2)
if v1 == v2:
    print("v1とv2は同じ")
else:
    print("v1とv2は違う値")

if v1 > 100:
    print("v1は100より大きい")
elif v1 > 50:
    print("v1は50より大きい")
else:
    print("v1は50以下")

if 100 >= v1 >= 50: print("v1は100から50の間")

# 要素を調べる
l = [1, 2, 3]
if 3 in l: print("3はlの中にある")

if 9 not in l: print("9はlの中にない")

s2 = "v1は50未満" if v1 < 50 else "v1は50より大きい"
print(s2)

# forループ
lst = [1, 2, 3, 4, 5, 6]
for l in lst:
    print(l)

# range
for count in range(10):
    print(count)

# range(開始数, 終端, 倍数)
for count in range(2, 10, 2):
    print(count)

# for else
for count in range(5):
    print(count)
else:
    print("ループ終了")

# whileループ
count = 0
sum = 0
while count <= 10:
    sum += count
    count += 1

print(sum)

# break,continue
sum = 0
for count in range(10):
    if count == 5: break
    sum += 1

print(sum)

sum = 0
for count in range(10):
    if (count % 2): continue
    sum += 1

print(sum)

# enumerate
lst = ["あ", "い", "う", "え", "お"]
for index, s in enumerate(lst):
    print(str(index) + ":" + s)

# zip
ilst = [1, 2, 3, 4, 5]
for (index, s) in zip(ilst, lst):
    print(str(index) + ":" + s)

# 例外
try:
    score = int("数字")
except ValueError:
    print("scoreは数値ではない")
else:
    print("例外は発生しなかった")

