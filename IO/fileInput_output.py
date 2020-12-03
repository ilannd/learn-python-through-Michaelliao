#  读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
#  所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），
#  或者把数据写入这个文件对象（写文件）

"""
f=open('test01.txt','r')   #  open函数传入传入文件名和标示符
print(f.read())   #  read方法可以一次读取文件的全部内容，python把内容读取到内存，用一个str表示
f.close()
"""

"""
try:
    f = open('test01.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
#  由于文件读写时非常可能产生IOError，一旦出错，后面的f.close()就不会调用，文件无法正常关闭
"""

# 每次这么写太繁琐了，引入with语句来自动帮我们调用close()方法

with open('test01.txt', 'r') as f:
    print(f.read())

#  反复调用read(size)方法，每次最多读取size个字节的内容。
#  另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
#  因此，要根据需要决定怎么调用
#  如果文件很小，read()一次性读取最方便；
#  如果不能确定文件大小，反复调用read(size)比较保险；
#  如果是配置文件，调用readlines()最方便
'''
f = open('test01.txt', 'r')
for line in f.readlines():
    print(line.strip())  # 把末尾的\n去掉
f.close()
'''

'''
f = open('test01.txt', 'r')
print(f.readline())  # 只能读一行
f.close()
'''

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。


f = open('situation.jpg', 'rb')   #  要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
print(f.read())  # 打印出十六进制表示的字符
f.close()


with open('gbk.txt', 'r', encoding='utf-8', errors='ignore') as f:
    print(f.read())

#  当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，
#  操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险
with open('test01.txt', 'a') as f:
    f.write('吕玉玺')
    # print(f.read())   # 这样写不行，使用write写入一个字符串，但是此时并没有真正的写入，而是还存在于内存中。此时执行read读取的为空字符。
    # 需要执行f.close()以后，再使用f=open(“test01.txt”)
    # f.read()才能够读取到数据。
    # 你是用open打开一个文件，此时调用的是w写入模式，下面使用read是没有权限的，你得使用w+读写模式
with open('test01.txt', 'r') as f:
    print(f.read())
# 写完后关掉再去读
# w模式写文件，会覆盖掉原来的文件的内容
# 住家文件用a 模式
