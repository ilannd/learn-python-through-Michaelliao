print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
f = lambda x: x * x
print(f)
print(f(5))


def build(x, y):
    return lambda: x * x + y * y


print(build(2, 3)())

'''def now():
    print('2020 - 10 - 6')


f = now
print(f())

print(now.__name__)
print(f.__name__)'''

'''def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)  # 这里又调用原始函数

    return wrapper


@log  # 相当于执行了   now=log(now)
def now():
    print('2020-10-6')


print(now())'''

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')  # 相当于执行了   now=log('execute')(now)
def now1():
    print('2020-10-6')


print(now1())
print(now1.__name__)  # 如果没有functools.wraps，它的__name__是wrapper


