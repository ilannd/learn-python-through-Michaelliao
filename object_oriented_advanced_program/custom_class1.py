#  __getattr__


class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25  # 也可以返回函数


#  注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找

s = Student()
print(s.name)
# print(s.score)  # 当调用类的属性或方法时，如果不存在，就会报错


#  要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性

print(s.score)  # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
print(s.age())  # 返回函数时要变一下返回方式
print(s.abc)  # 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None


#  要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误


class Student1(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 26
        raise AttributeError('\'Student1\' object has no attribute \'%s\'' % attr)


s1 = Student1()
print(s1.age())


# print(s1.name)  #抛出异常


#  这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
#
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用


# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
#
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

class Student2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s2 = Student2('Mjsjjs')
print(s2())  # self参数不要传入

#  __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别
#  判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例


print(callable(Student()))  # 我运行出来是False,但是网站上写的是True
print(callable(max))
print(callable([1, 2, 3]))

#  通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
