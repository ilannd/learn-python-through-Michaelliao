def fun(step):
    num = 1
    num += step
    print(num)


i = 1
while i < 5:
    fun(3)
    i += 1


# 连续调用函数4次，每次输出的值都是4，即3+1，这说明每次调用fun函数之后，函数内部定义局部变量num就被销毁了，
# 没有保存下来，说明函数的局部作用域被销毁了。如果没有被销毁，会在4的基础上继续加。那如果要保存函数的局部变量，怎么办呢？引入“闭包”
# num 是局部变量
# 装饰器的本质也是闭包

# “闭包”的本质就是函数的嵌套定义，即在函数内部再定义函数

# “闭包”有两种不同的方式，第一种是在函数内部就“直接调用了”；第二种是“返回一个函数名称”


# （1） 直接调用
def Maker(name):
    num = 100

    def func1(weight, height, age):
        weight += 1
        height += 1
        age += 1
        print(name, weight, height, age)

    func1(100, 200, 300)


Maker('feifei')


#  (2) 返回函数名称
def Maker1(name):
    num = 100

    def func1(weight, height, age):
        weight += 1
        height += 1
        age += 1
        print(name, weight, height, age)

    return func1  # 此处不直接调用，而是返回函数名称（Python中一切皆对象)


maker = Maker1('lele')  # 调用包装器
print(maker(100, 200, 300))  # 调用内部函数


# (3)  闭包”的作用——保存函数的状态信息，使函数的局部变量信息依然可以保存下来
def Maker2(step):  # 包装器
    num = 1

    def fun1():  # 内部函数
        nonlocal num  # nonlocal关键字的作用和前面的local是一样的，如果不使用该关键字，则不能再内部函数改变“外部变量”的值
        num = num + step  # 改变外部变量的值（如果只是访问外部变量，则不需要适用nonlocal）
        print(num)

    return fun1


j = 1
func2 = Maker2(3)   # 调用外部包装器
while j < 5:
    func2()   # 调用内部函数4次，输出的结果是4,7,10,13
    j += 1
