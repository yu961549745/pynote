'''
函数式编程
1. 高阶函数
2. 返回函数
3. 匿名函数
4. 装饰器
5. 偏函数
'''

#%% 高阶函数
# 所谓高阶函数，就是能够接收函数作为输入的函数
# Python的函数其实也是一个对象


def feval(a, b, f):
    return f(a) + f(b)


print(feval(1, -2, abs))

# map/reduce

# map 类似于 Maple 的 map 函数
# 但是需要转化成 list 获取值
# 另外，还能引入一下Python的lambda表达式
# lambda arg1,arg2,...:returnExpression
print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))

# reduce 接收一个两个输入参数的函数
# reduce(f,[x1,x2,x3])=f(f(x1,x2),x3)
from functools import reduce
print(reduce(lambda x, y: 10 * x + y, [1, 2, 3, 4, 5, 6]))

# filter 具有筛选的功能
# 依然需要list之后获取结果
print(list(filter(lambda x: x % 2 == 0, list(range(10)))))

# sorted 实现排序功能
L = [2, 3, 5, -1, -2]
print(sorted(L))
print(sorted(L, key=abs))
print(sorted(L, reverse=True))

#%% 返回函数
# python 也能将函数作为返回值
# 可以实现一些惰性求值的功能


def lazy_sum(*args):
    def f():
        s = 0
        for x in args:
            s += x
        return s
    return f


f = lazy_sum(1, 2, 5)
print(f())
# 这种形式被称为是函数闭包
# 在使用必报时，要牢记返回函数并未被求值
# 因此切忌引用可能发生变化的变量，如：循环变量等


def count():
    "反例"
    fs = []
    for i in range(3):
        def f():
            return i**2
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def count():
    "正确方式"
    def g(i):
        def f():
            return i * i
        return f
    return [g(i) for i in range(3)]


f1, f2, f3 = count()
print(f1(), f2(), f3())

#%% 匿名函数
# 即：lambda 表达式
# lambda arg1,arg2,...:returnExpression

#%% 装饰器
# 本质上，装饰器就是一个返回函数的函数


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log  # 利用 python 语法等价于  now=log(now)
def now():
    print('2017')


now()
print(now.__name__)

# 更复杂的具有参数的装饰器

import functools


def log(text='call'):
    def decorator(func):
        @functools.wraps(func)  # 表示返回函数的 __name__ 依然是传入函数的名字
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        # 等价于
        # wrapper.__name__=func.__name__
        return wrapper
    return decorator


@log('execute')  # 利用 python 语法等价于  now=log('exeute')(now), 正因为这个语法，所以需要嵌套两层
def now():
    print('2017')


now()
print(now.__name__)

#%% 偏函数
# 就是把函数的某些参数固定下来，返回一个功能更简单的函数
import functools
int2 = functools.partial(int, base=2)
print(int2('1000'))
