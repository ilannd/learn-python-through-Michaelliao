#!/user/bin/env python3
# -*- coding:utf-8 -*-

'a test model'

__author__ = 'Lv YUxi'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':  # 当我们在命令行运行这个模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
    test()

print(__doc__, __author__)


def _private_1(name):  # _parvate_1()函数是私有的
    return 'Hello,%s' % name


def _private_2(name):  # _private_2()函数是私有的
    return 'Hi,%s' % name


def greeting(name):    # greeting函数是公开的，而其内部逻辑是私有的，外部要引用的定义为public,不引用的定义为private
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


print(greeting('Lv YU Xi'))
print(greeting('Lv'))