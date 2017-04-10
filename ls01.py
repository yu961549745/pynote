#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
第一节
+ Python解释器
+ Python运行
+ Python输入输出
+ Python字符串
+ Python整数和浮点数
'''
#%% Python 解释器
# Python拥有许多解释器
# + CPython 是默认的python解释器，用C语言编写。
# + ipython 基于 CPython 的交互式解释器
# + PyPy 采用JIT（动态编译）方法，加速Python运行
# + JPython 可以把 python 代码编译成 java 字节码，在JVM上运行
# + IronPython 把 python 编译成 .NET

#%% 运行相关
#!/usr/bin/env python3
# 配合
# $ chmod a+x ls01.py
# 可以直接运行
# 上面的写法表示从系统的环境变量里搜索 Python3
# 而
# !/usr/bin/python
# 则要/usr/bin下一定要有python
# Python3 默认支持 UTF8，而 Python2 还需要自己指定
# 如下写法是python2
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 但是装了插件之后完全不需要这么麻烦呢
import sys
print(sys.version)
print('hello world')

#%% 输出
# 特点是默认一个 print 都是自带换行的呢
# 对于输出，除了默认的方法
print('hello')
# 还有一些Python特有的输出方法
# 1. 多个字符串用一个 print 输出，会用空格连接
print('hello', 'world')
# 2. 可以指定字符串不转义
print('\n', r'\n')
# 3. 可以支持多行字符串，原来这个不是注释是多行字符串啊，震惊！但是也常用作多行注释
print('''UC
震惊部报道''')

#%% 输入
# 关于输入的话，简单的形式就是
# 输入的内容是字符串
x = input()
print(x)
# 更加友好一点，还能增加提示
x = input('please input integer : ')
print('Input is', x)

#%% 字符串
# 单引号和双引号都可以，当字符串中有一种引号时，使用另一种引号则不需要转义
print('"haha"', "I'm OK")
# 以及上一节介绍的指定不转义和多行字符串
print(r'快来\n', '''UC
震惊部报道''')
# 转义规则，和C语言相同
# 格式化采用 % 连接字符串和元组
print('%d %s' % (1, 'abc'))
# 字符编码
# b'...' 表示一个 bytes 数组
# 对 bytes 和 str 使用 len() 函数可以分别得到 字节数 和 字符数
x = '中文'.encode('utf-8')
y = x.decode('utf-8')
print(x, len(x))
print(y, len(y))
# ord 和 chr 函数实现字符和 unicode 的转换
x = ord('中')
print(x)
print(chr(x))

#%% 布尔变量
# 逻辑操作回布尔变量
# True False 注意大小写
# 逻辑运算 and or not
print(True, False, True and False, not False, 1 > 2)

# Python 不能直接声明常量

#%% 整数，浮点数
# 和C不同的是，Python的/默认采用浮点数的除法
# 而 // 才是整数的除法
# 另外一个特有的操作是 ** 表示幂次
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(2**10)
