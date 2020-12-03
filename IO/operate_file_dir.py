# Python内置的os模块也可以直接调用操作系统提供的接口函数
import os

print(os.name)  # 操作系统类型 nt为windows操作系统
# print(os.uname())  # uname函数造windows上不支持,返回系统的详细信息
print(os.environ)  # 获取系统的环境变量
print(os.environ.get('PATH'))

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下
print(os.path.abspath('.'))



# 先到这，作者演示的是linux路径格式,有点问题出错了
