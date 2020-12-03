class Student(object):
    def __init__(self, name, score):  # __init__方法的第一个参数永远都是self,表示创建的实例本身        仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
        self.__name = name  # 把各种属性绑定到self，因为self 就指向创建的实例本身
        self.__score = score

    # 比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

    def print_score(self):  # 类的方法，第一个参数必须是self
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):  # 私有变量的值通过get函数来获取
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):  # 通过set函数来对私有变量进行修改
        self.__name = name

    def set_score(self, score):  # 可以在set函数里对参数进行检查，避免传入无效参数
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)  # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python
# 解释器自己会把实例变量传进去
lisa = Student('Lisa Simpson', 87)
print(bart.print_score(), bart.get_grade())
print(lisa.print_score(), lisa.get_grade())
# print(bart.__name)    #访问不了私有变量
print(bart.get_name())
# bart.set_name('Baaaa wjsj')   #通过set函数来对私有变量进行修改
# print(bart.get_name())
print(bart._Student__name)  # 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量，，，，强烈不建议这样做
bart.__name = 'New Name'  # 虽然看着好像成功的修改了__name的值，但是这个__name和class内部的__name变量不是一个变量，因为它已经被python解释器自动改成了_Student__name
print(bart.__name)
print(bart.get_name())
