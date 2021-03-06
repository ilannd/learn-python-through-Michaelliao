g = (x for x in range(1, 11))
print(g)
print(next(g))  # 每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
for n in g:  # 生成器也是可迭代对象,通过for循环来迭代它，并且不需要关心StopIteration的错误
    print(n)

# 生成器是用来创建迭代器的简单而强大的工具
# 生成器能做到迭代器能做的所有事,而且因为自动创建了 iter()和 next()方法,生成器显得特别简洁,而且
# 生成器也是高效的，使用生成器表达式取代列表解析可以同时节省内存。除了创建和保存程序状态的自动方法,当
# 生成器器终结时,还会自动抛出 StopIteration 异常
