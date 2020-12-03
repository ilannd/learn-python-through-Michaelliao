print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))


def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))

import functools

int2 = functools.partial(int, base=2)  # 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
print(int2('1000000'))
print(int2('10000', base=10))

max2 = functools.partial(max, 10)  # 相当于把10作为参数的一部分自动加到左边，相当于在10,5,6,7里面选取最大值
print(max2(5, 6, 7))
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单
