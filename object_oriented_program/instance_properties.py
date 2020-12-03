class Student(object):
    pass


s = Student()
s.name = 'Michael'
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 这是给一个实例绑定的方法，对另外一个实例是不起作用的

s2 = Student()


# s2.set_age(23)
# print(s2.age)


# 为了给所有实例绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

# set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
