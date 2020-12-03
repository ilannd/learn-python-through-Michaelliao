try:
    print('try......')
    r = 10 / int('2')
    print('Result:', r)
except ValueError as e:  # Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽
    print('Value Error:', e)
except ZeroDivisionError as e:  # 如果没有错误发生，except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）
    print('ZeroDivisionError:', e)
else:
    print('No error')
finally:
    print('finally....')
print('END')
# 捕获错误时，如果想精确的捕获错误，就把小错误的类写在前面，如果把父类错误写在前面，就永远也不可能捕获子类错误
# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，只要main()捕获到了，就可以处理
#  不需要在每个可能出错的地方去捕获错误，在合适的层次捕获错误就行


#  如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
#  出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置
#  既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去
# 记录错误
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:  # 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
        logging.exception(e)


print(main())
print('END')


'''# 抛出错误
def foo1(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value:%s' % s)
    return 10 / n


def bar1():
    try:
        foo1('0')
    except ValueError as e:
        print('ValueError')
        raise


#   raise语句如果不带参数，就会把当前错误原样抛出

print(bar1())
#  在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
#   其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的
#   方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理
'''