# 関数
def sumsample(a, b):
    return a + b


print(sumsample(1, 2))

# キーワード引数
s = sumsample(a=1, b=2)
print(s)


v = 1
def scope_v1():
    v = 10
    print("scope_v内部 : ", v)

scope_v1()
print("外部 : ", v)

# グローバル
v = 1
def scope_v2():
    global v
    v = 20
    print("scope_v内部 : ", v)

scope_v2()
print("外部 : ", v)


# 可変長引数

def argfunc1(*arg):
    print(arg)

argfunc1(1, 2, 3, 4)

def argfunc2(*arg1, arg2):
    print(arg1, arg2)

argfunc2(1, 2, 3, arg2 = 4)


# キーワード引数を辞書として受け取る
def dicfunc(**arg):
    print(arg)

dicfunc(name="あいうえお", num = 1)

# Lambda
sample = lambda a,b: a + b
print(sample(1,2))

sum2 = lambda *nums: sum(nums)
print(sum2(1,2,3,4,5))

# map

lst = [1,2,3,4,5]
def to_x10(n):
    return n*10

for num in map(to_x10, lst):
    print(num)

lst = list(map(lambda n: n*10, lst))
print(lst)

lst = [n * 10 for n in lst]
print(lst)


# filter
lst = [1,2,3,4,5]
res = []
for n in filter(lambda n:n > 2, lst):
    res.append(n)
print(res)

res = [n for n in lst if n > 2]
print(res)


# sort
lst1 = ["Abc", "ab",  "dEf", "Dg", "Ghi", "gh", "ghi", "bcd"]
lst2 = sorted(lst1, key=str.upper)
print(lst2)

lst2 = sorted(lst1, key=lambda s : s[0])
print(lst2)

lst2 = sorted(lst1, key=lambda s : s[0], reverse=True)
print(lst2)

