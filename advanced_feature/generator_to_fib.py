def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # yield关键字把普通函数变为一个generator
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
while True:
    try:
        x = next(f)
        print('f', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
