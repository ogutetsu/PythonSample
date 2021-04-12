



class Counter:
    count = 0
    name = "Counter Class"
    # カプセル化
    __c_num = 111

    # コンストラクタ
    def __init__(self, num):
        self.num = num

    def inc(self):
        Counter.count += 1

    # pass 実体のないメソッド
    def dec(self):
        pass

    # プロパティ
    __pnum = 22
    def get_pnum(self):
        return self.__pnum
    def set_pnum(self, num):
        self.__pnum = num
    pnum = property(get_pnum, set_pnum)


# クラスの継承
class TimeCounter(Counter):
    def __init__(self, num):
        self.num = num


c = Counter(0)
print(c.num)
c.inc()
print(c.count)


# 空クラス
class PassClass:
    pass

# インスタンス変数を動的に追加
c.addnum = 10
print(c.addnum)

# クラス変数を動的に追加
Counter.classValue = 100
print(c.classValue)

# メソッドを動的に追加
def add_method(self):
    print("{}".format(self.name))

Counter.add_method = add_method

c.add_method()


# プロパティ
print(c.pnum)
c.pnum = 11
print(c.pnum)



