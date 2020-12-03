# 如果我们想限制实例的属性，比如，只允许对Student实例添加name和age属性，，使用__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'Michael'
s.age = 25


# s.score = 99  # 不能绑定score


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 99
print(g.score)

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
