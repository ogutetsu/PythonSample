
# -------------
# strクラス
s = "Hello"
print(s.upper())    # 文字列を大文字に変換
print(s.lower())    # 文字列を小文字に変換
print(s.count('l')) # 指定した文字列が出現する個数
print(s.endswith('lo')) # 指定した文字列で終わっているか
print(s.find('e')) # 指定した文字列が含まれていれば位置インデックスを返す
print(s.replace('H', 'h')) # 指定した文字列を置換
print(s.startswith('H')) # 指定した文字列で始まっているか

s = ''
lst = ['H', 'e', 'l', 'l', 'o']
print(s.join(lst)) # 文字列の連結

s = "H,e,l,l,o"
print(s.split(',')) # セパレータで分割

s = "Hello"
print(s[0:2]) # 指定範囲の文字列を取得
print(s[3:])  # 終端を省略


s = "Hello {}!".format("World")
print(s)

s = "{} {}!".format("Hello", "World")
print(s)

s = "{1} {0}".format("World", "Hello")
print(s)

# 小数点第3位まで表示
s = "{:.3f}".format(10/3)
print(s)

# 3桁区切り
s = "{:,}".format(111111111)
print(s)


#--------------
# リストとタプル

lst = [1, 2] + [3, 4]
print(lst)

lst = [1] * 4
print(lst)

lst = [1, 2, 3, 4]
print(lst.index(3))

lst[0] = 10
print(lst)

lst.append(5)
print(lst)

lst.remove(10)
print(lst)

del lst[0]
print(lst)

lst.reverse()
print(lst)

print(max(lst))
print(min(lst))
print(sum(lst))

lst.sort()
print(lst)

print(sorted(lst))

# 内包記述
lst = [c ++ 2 for c in range(0,10)]
print(lst)

week = [day + "曜" for day in "月火水木金土日"]
print(week)

lst = [n for n in range(0, 10) if (n % 2) == 0]
print(lst)

# タプルの要素から条件に合うリストを作成
tests = [(30, "赤点"),(80, "合格"),(10, "赤点"),(100,"合格")]
success = [t[0] for t in tests if t[1] == "合格"]
print(success)


#------------
# Dictionary

colors = {"red":"赤","green":"緑","blue":"青"}
print(colors)
print(colors["red"])

del colors["blue"]
print(colors)

print("red" in colors)

print(colors.keys())
print(colors.values())

print(colors.items())

# 内包表記
colors = ["赤","緑","青","黄"]
color_dic = {color:0 for color in colors}
print(color_dic)
colors_num = [1, 2, 3, 4]
color_dic = {a:b for(a,b) in zip(colors, colors_num)}
print(color_dic)

# 値とキーの入れ替え
color_dic2 = {b:a for(a,b) in color_dic.items()}
print(color_dic2)



#-----------------
# 集合
s = {"赤","緑","青","黄","赤"}
print(s)
lst = [1,2,3,4,5,2,3,1]
s = set(lst)
print(s)
s.add(6)
print(s)
s.remove(1)
print(s)

s1 = {"赤","緑","青","黄"}
s2 = {"白","黒","緑","黄"}

print(s1 | s2)
print(s1 & s2)
print(s1 ^ s2)
