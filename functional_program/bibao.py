def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


print(calc_sum(1, 3, 5, 7, 9))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)  # 返回False,当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)  # 并非立即执行
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def count1():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # 立即执行
    return fs


c1,c2, c3 = count1()
print(c1(),c2(), c3())
