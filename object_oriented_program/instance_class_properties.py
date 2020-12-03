class Student(object):
    name = 'Student'  # 定义一个类属性

    # def __init__(self, name):
    # self.name = name    #定义一个实例属性


s = Student()
# s = Student('Bob')
s.score = 90
print(s.name)  # 定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
print(Student.name)
s.name = 'Michanel'
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)
del s.name
print(s.name)  # 实例的name属性没有找到，类的name属性就显示出来了

# 千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
