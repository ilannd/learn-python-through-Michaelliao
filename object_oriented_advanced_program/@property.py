# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
# 类似于前面的私有属性
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must in 0-100')
        self._score = value


s = Student()
s.set_score(99)
print(s.get_score())


# s.set_score(1000)   #类里面有进行参数检查


#  有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的
#  对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student1(object):

    @property  # 把一个getter方法变成属性，只需要加上@property就可以了
    def score(self):
        return self._score

    @score.setter  # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s1 = Student1()
s1.score = 60  # OK，实际转化为s.set_score(60)
print(s1.score)  # OK，实际转化为s.get_score()


# s1.score = 999


# 在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的


# 还可定义只读属性
class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter  # birth是一个可读写的属性
    def birth(self, value):
        self._birth = value

    @property  # age是一个只读属性  age可以根据birth和当前时间计算出来
    def age(self):
        return 2015 - self._birth

#  小结：@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
