from object_oriented_program import subclass

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(subclass.an))
print(type(subclass.cat))

# 判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10)) == types.GeneratorType))
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数,,,在subclass那个模块有写


# 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”

print(dir('ABC'))  # 要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
# print(getattr(obj,'z'))  #试图获取不存在的属性，抛出异常
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
