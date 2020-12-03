#  如果按照常识那样一直继承下去，类的数量会成指数增长，这样设计不合理
#  正确的设计是采用多重继承
from socketserver import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class FlyableMixIn(Animal):
    def fly(self):
        print('Running....')


class RunnableMixIn(Animal):
    def run(self):
        print('Flying.....')


class Dog(Mammal, RunnableMixIn):  # 多重继承，一个子类就可以同时获得多个父类的所有功能
    pass


class Bat(Mammal, FlyableMixIn):  # MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
    pass


class Parrot(Bird,
             FlyableMixIn):  # Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来
    pass


class Ostrich(Bird, RunnableMixIn):
    pass


d1 = Dog()
print(d1.run())


class MyTCPServer(TCPServer, ForkingMixIn):
    pass


class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

# class MyTCPServer(TCPServer, CoroutineMixIn):   #这里是想继承协程，但好像无法导入
#    pass


#  Java是单一继承的语言
