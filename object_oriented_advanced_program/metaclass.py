#  动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
class Hello(object):
    def hello(self, name='world'):
        print('Hello,%s' % name)
    #  假设上面的Hello类是定义在hello.py模块里面的，当python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class的对象


h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))


#  type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello

# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name='world'):
    print('Hello,%s' % name)


Hello1 = type('Hello1', (object,), dict(hello=fn))  # 创建Hello class  参数一：类的名称    参数二：继承的父类集合  参数三： 类的方法名称与函数绑定
h1 = Hello1()
print(h1.hello())
print(type(Hello1))
print(type(h1))
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同


#  metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
#
# metaclass，直译为元类，简单的解释就是：
#
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
#
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
#
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
#
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
#
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。

# 所以这一块我不想学了，拜拜
