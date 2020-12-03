# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict
d = dict(name='Bob', age=20, score=90)
#  可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，
#  下次重新运行程序，变量又被初始化为'Bob'


#  我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
#  序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
#  反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling


# Python提供了pickle模块来实现序列化
import pickle

d = dict(name='Bob', age=20, score=90)
print(pickle.dumps(d))  # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
'''f = open('dump.txt', 'wb')
pickle.dump(d, f)  # pickle.dump()直接把对象序列化后写入一个file-like Object
f.close()'''

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
print(pickle.loads(
    b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KZu.'))
'''f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()'''
# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已

# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
# 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json

d1 = dict(name='Bob', age=20, score=90)
print(json.dumps(d1))  # 把python对象变成一个JSON，dumps()方法返回一个str，内容就是标准的JSON

# dump()方法可以直接把JSON写入一个file-like Object


# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age":20,"scor":88,"name":"Bob"}'
print(json.loads(json_str))
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换


# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.score = score
        self.age = age

    def __str__(self):
        return 'Student object (%s,%s,%s)' % (self.name, self.age, self.score)


s = Student('Bob', 20, 99)


# print(json.dumps(s))  # TypeError,Student对象不是一个可序列化为JSON的对象
# 默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可


# print(json.dumps(s, default=student2dict))  # 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
def student2dict(s):
    return {
        'name': s.name,
        'age': s.age,
        'score': s.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

std_data = json.dumps(s, default=student2dict)
# std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print(std_data)
# rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
rebuild = json.loads(std_data, object_hook=dict2student)
print(rebuild)
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
