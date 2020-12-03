# __str__
#  形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的
#  除了__slots__和__len__()，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 使打印输出类似 Student object (name:Michnel)
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__  # 这样在命令行输出也可以了


print(Student('Michnel'))  # 未添加__str__方法时打印的输出不好看，打印出一堆<__main__.Student object at 0x109afb190>


#  如果在命令行直接输出s   (s=Student('ssjj')),, 打印输出的还是一对不好看的
# 是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

# __iter__
#  如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
#  拿到循环的下一个值，直到遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a  # 返回下一个值


for i in Fib():
    print(i)


#  __getitem__

# print(Fib()[5])  #  Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素就会报错

#  要表现得像list那样按照下标取出元素，需要实现__getitem__()方法


class Fib(object):
    def __getitem__(self, n):  # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[0])
print(f[100])


# list能用切片，对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断

class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib1()
print(f[0:5])
print(f[:10])
#  但是没有对step参数作处理,也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
#
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
#
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口



