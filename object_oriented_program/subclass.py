class Animal(object):
    def run(self):
        print('Animal is running......')


class Dog(Animal):
    def run(self):
        print('Dog is running.....')  # 子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态

    def eat(self):
        print('Eating meat....')


class Cat(Animal):
    def run(self):
        print('Cat is running.....')


an = Animal()
dog = Dog()
print(dog.run())

cat = Cat()
print(cat.run())
print(isinstance(dog, Dog))
print(isinstance(cat, Cat))
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))  # 一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
print(isinstance(an, Dog))  # 但反过来不行


def run_twice(animal):
    animal.run()
    animal.run()


# 新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态
print(run_twice(Animal()))
print(run_twice(Dog()))  # 传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思
print(run_twice(Cat()))
# 多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则
#  开闭原则：对扩展开放：允许新增Animal子类；   对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
'''python是动态语言，不一定需要传入Animal类型。对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法.
我们只需要保证传入的对象有一个run()方法就可以了动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只
要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象'''