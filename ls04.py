'''
高级特性
1. 切片
2. 迭代
3. 列表生成式
4. 生成器
5. 迭代器
'''

#%% 切片
# 类似于 Matlab 的冒号表达式，区别在于
# 开始 : 结束 : 间隔
# 同时支持负数索引
# 可以省略任意元素

L = list(range(100))
print(L[0:10])
print(L[90:-1])
print(L[95:])
print(L[:10])
print(L[:10:2])
print(L[:])

#%% 迭代

# 普通迭代
L = {'a': 1, 'b': 2, 3: 3}
for k in L:
    print(k, L[k])

# 键值迭代
for k, v in L.items():
    print(k, v)

# 下标迭代
L = [1, 2, 3, 4, 5]
for i, v in enumerate(L):
    print(i, v)

#%% 列表生成式
# 单变量单层生成式
print([x**2 for x in list(range(10))])
# 多变量单层生成式
print([x + '=' + v for x, v in {'a': 'X', 'b': 'y'}.items()])
# 双层生成式
print([x + y for x in range(3) for y in range(4)])
# 条件生成式
L = ['Hello', 'World', 18, 'Apple', None]
L1 = [x.lower() for x in L if isinstance(x, str)]
print(L1)

#%% 生成器
# 采用生成器而不采用列表，可以节省内存
# 适用于只按顺序访问一次的情形

# 列表生成器
# 将列表生成式的中括括号改为圆括号即可
g = (x**2 for x in range(10))
for x in g:
    print(x)

#%% 函数生成器
# 函数生成器和普通函数的区别在于 yield 替代了 return
# 当函数运行到 yield 时返回值
# 下次调用时从 yield 处继续执行


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


g = fib(10)
for x in g:
    print(x)

#%% 迭代器
# 可以被在for循环中使用的都是 Iterable
# 生成器是 Iterator
# list , set , dict , str 虽然 Iterable 但不是 Iterator
from collections import Iterable
from collections import Iterator
print(isinstance({}, Iterable))
print(isinstance({}, Iterator))
print(isinstance(range(10), Iterable))
print(isinstance(range(10), Iterator))
print(isinstance((x for x in range(3)), Iterator))
