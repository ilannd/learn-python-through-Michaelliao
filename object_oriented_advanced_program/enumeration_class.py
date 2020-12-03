# 通过  JAN = 1  这种方式来定义常量，简单，但是类型是 int，并且仍然是变量
#  更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#  我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # 输出是这样的：Jan => Month.Jan , 1
#   value属性则是自动赋给成员的int常量，默认从1开始计数

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique


@unique  # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5  # 刚才打错了，设为4了，出现了成员值相同的情况，报错了  ValueError: duplicate values found in <enum 'Weekday'>: Fri -> Thu
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(1))
#  print(Weekday(7))
for name, member in Weekday.__members__.items():
    print(name, '=>', member)
