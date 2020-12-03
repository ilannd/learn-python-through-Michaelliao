#  很多时候，数据读写不一定是文件，也可以在内存中读写
#  StringIO顾名思义就是在内存中读写str
from io import StringIO

#  要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())  # getvalue()方法用于获得写入后的str

#  要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
from io import StringIO

f = StringIO('Hello\nHi\nGoodbye')
while True:
    s = f.readline()
    if s == '':  # 这里一定不要写成s==' ',这样程序结束不了了
        break
    print(s.strip())

#  StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
#  BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))  # 请注意，写入的不是str，而是经过UTF-8编码(encode)的bytes
print(f.getvalue())

from io import BytesIO

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')  # 别忘记前面的b
print(f.read())  # 输出还是\xe4\xb8\xad\xe6\x96\x87
# 只有类文件对象才有read()方法
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
