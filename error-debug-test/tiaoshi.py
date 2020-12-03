#   需要一套调试程序的手段来修复bug
#   第一种简单粗暴地方法就是直接把有问题的变量用print打印出来，用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息
#    凡是用print（）来辅助查看的地方，都可用断言来代替

# 第二种 断言
'''def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'  # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
    return 10 / n


#  如果断言失败，assert语句本身就会抛出AssertionError
def main():
    foo('0')


#  程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert
# 注意 : 断言的开关"-O" 是英文大写字母O，不是数字0       没关报错是：AssertionError: n is zero       关掉之后就报错：ZeroDivisionError: division by zero
main()

# 别忘记调用主函数，否则怎么运行呀，切记切记
'''
# 第三种 logging
#  把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
import logging

logging.basicConfig(level=logging.INFO)  # logging.info()就可以输出一段文本，在错误信息中会增加输出一行 INFO:root:n = 0
s = '0'
n = int(s)
logging.info('n=%d' % n)
print(10 / n)
# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
# 第四种，启动Python的调试器pdb，让程序单步运行，可以随时查看运行状态

# 没必要学这个，用ide的的断点就很好
