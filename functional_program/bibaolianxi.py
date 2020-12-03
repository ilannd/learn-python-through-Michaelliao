#  这种是可以测试通过的
'''def createCounter():
    cnt = [0]  # 传的cnt是一个列表的话,其实本质上传递的是一个地址,在这个地址上我们可以做任意改变.只要这个列表还是这个列表,他的地址就不会变.利用这种特性,我们就可以随便折腾了

    def counter():
        cnt[0] = cnt[0] + 1
        return cnt[0]

    return counter'''


#  这种是可以测试通过的
def createCounter():
    cnt = 0

    def counter():
        nonlocal cnt  # 参考add_to_bibao.py里面的nonlocal的用法，可以对cnt进行修改      那篇博客里面还讲到了重新定义变量，或者使用global关键字   让“内部函数”可以修改“外部函数（装饰器）”的局部变量值
        cnt = cnt + 1
        return cnt

    return counter  # 不直接调用，返回函数名称


#  怕的时候出错了，报错说我全局变量未定义
'''def createCounter():
    cnt = 0

    def counter():
        global cnt
        cnt = cnt + 1
        return cnt

    return counter'''

# 测试失败
'''def createCounter():
    cnt = 0

    def counter():
        cnt = 1  
        cnt = cnt + 1
        return cnt

    return counter  
# 这样的话返回值是2,2,2,2,2,说明每次调用函数之后，函数内部定义局部变量cnt就被销毁了'''

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  #
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:

    print('测试通过')
else:
    print('测试失败')
