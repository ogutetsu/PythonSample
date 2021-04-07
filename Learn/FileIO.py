
#--------------
# ファイル読み込み

f = open("sample.txt", "r", encoding="utf_8")
print(f.read())
f.close()

# 2文字ずつ読み込む
f = open("sample.txt", "r", encoding="utf_8")
print(f.read(2))
print(f.read(2))
f.close()

# 行
f = open("sample.txt", "r", encoding="utf_8")
print(f.readlines())
f.close()

f = open("sample.txt", "r", encoding="utf_8")
for l in f.readlines():
    print("{}".format(l.strip("\n")))
f.close()

f = open("sample.txt", "r", encoding="utf_8")
for i, l in enumerate(f):
    print("{} : {}".format(i + 1, l.strip("\n")))
f.close()

# with

with open("sample.txt", "r", encoding="utf_8") as f:
    print(f.read())


#-------------
# ファイル書き込み

with open("write.txt", "w", encoding="utf_8") as f:
    f.write("Hello")
    f.write("Python!")

lst = ["こんにちは", "Python"]
with open("write.txt", "a", encoding="utf_8") as f:
    f.writelines(lst)

