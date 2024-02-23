

name = 'Test'
value = 1/3

# 文字列の書式設定
print('Hello %s' % name)
print('Hello format {}'.format(name))
print('Hello dict %(name)s' % {'name':name})
print('Hello format2 {name}'.format(name=name))

# 浮動小数点の書式
print('%.2f' % value)

# 変数を複数利用するケース
print('Hello {0}, value: {1:.3f}. Bye {0}'.format(name, value))

# f-string
name2 = 'sample'
a = 123
b = 456
dic = dict(a=a, b=b)

print(f'''a: {dic['a']}''')
print(f'''sum: {dic['a'] + dic['b']}''')
print(f'if : {a if a > b else b}')
print(f'min: {min(a,b)}')
print(f'upper : {name2.upper()}')
