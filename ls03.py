'''
函数
'''

#%% 函数调用
# Python的函数名是指向函数对象的一个引用，可以赋值给另一个变量
print(abs(-1))
a = abs
print(a(-1))

#%% 函数的定义
# def functionName(paramList):
# 空函数可以使用 pass 来保持结构完整


def func():
    return 1, 2


# Python可以实现多参数的返回，但是实际上返回的是一个 tuple
x, y = func()
z = func()
print(x, y, z)

#%% 函数的参数
'''
Python有以下几类参数：
1. 位置参数，即最普通的参数，例如 x
2. 默认参数，即带有默认值的参数，例如  x=233，注意默认值需要时不可变对象
3. 可变参数，*args
4. 关键字参数， **kwargs
5. 命名关键字参数，定义在可变参数之后的参数，若没有可变参数，则可以用 * 代替
'''


def testargs(a, b=1, *c, d=-1, **e):
    print(a, b, c, d, e)


# 命名关键字参数可以具有默认值，从而简化调用，否则将必须指定命名关键字参数的值
print(testargs(1))
print(testargs(1, 2))
# 可变参数相当于传递了一个 tuple
# 关键字参数相当于传递了一个 dict
print(testargs(1, 2, 3, 4, 5, d=5, f=4, g=6))
# 也可以通过传递 *tuple/*list 来替代可变参数，传入 **dict 来替代关键字参数
# 关键字参数在直接调用时，键本身是一个字符串，但可以简写成变量，而传递dict的键必须是字符串
print(testargs(1, 2, *(3, 4, 5), **{'d': 233, 'e': 244, 'f': 255, 1: 1}))
print(testargs(1, 2, *[3, 4, 5], **{'d': 233, 'e': 244, 'f': 255}))
