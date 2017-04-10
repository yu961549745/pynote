'''
第二节
+ list
+ tuple
+ dict
+ set
+ 条件语句
+ 循环语句
'''

#%% list
# list 可以包含任意元素
print([1, 2, 'hello', [1, 2]])
# 可以利用下标进行访问，从0开始，支持负数下标表示逆序访问
x = [1, 2, 3]
print(x[0], x[1], x[-1])
# 可以对元素进行拓展和插入
x.append(4)
x.insert(0, 0)
print(x)
# 可以对元素进行删除
x.pop()
print(x)
x.pop(0)
print(x)
# 直接通过赋值修改list
x[1] = 233
print(x)
# 还可以声明空list
x = []
print(len(x))
# 嵌套list可以用作多维数组
x = [[1, 2], [3, 4]]
for i in range(2):
    for j in range(2):
        print(x[i][j])

#%% tuple
# tuple 的功能类似于 list ，但它是不可变的
# 也可以通过和list一样的下标进行访问
# 特别需要声明的是，声明只有一个元素的tuple需要添加额外的逗号
x0 = ()
x1 = (1,)
x2 = (1, 2, 'hello')

#%% dict 是 Python 的 hask map
# 可以采用初始化，赋值的方式增加键值映射
# 其键可以是不同类型的值
x = {'a': 1, 'b': 2}
x[1] = 4
print(x)
# 不能使用不存在的键执行下标表达式
# 可以用 in 来判断是 dict 是否存在某个键
if '233' in x:
    print(x['233'])
else:
    print('233 not exist')
# 也可以使用 get 方法，同时可以指定默认返回值
print(x.get('233'), x.get('233', -1))
# 可以用 pop 删除键
x.pop('a')
print(x)
# dict 的遍历
# 默认按键遍历
for key in x:
    print(key, x[key])
# 可以用个items 方法进行键值的遍历
for k, v in x.items():
    print(k, v)

#%% 自定义对象作为键


class foo(object):
    def __init__(self, name):
        self.name = name


class stu(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):  # 等价于java 的 hashCode 方法
        return hash(self.name)

    def __eq__(self, other):  # 等价于 java 的 equals 方法
        return self.name == other.name

    def __repr__(self):  # 等价于 java 的  toString 方法
        return '(Stu:%s,%d)' % (self.name, self.age)


print({stu('a', 1): 233})
print({foo('233'): 233})
# print({[1, 2]: 3}) # list 不能作为键

#%% set
# 初始化
s = set([1, 2, 3, 3])
print(s)
# 可以用 add 和 remove 方法来增加和删除元素
s.add(4)
s.remove(1)
print(s)
# 还可以使用 & 和 | 进行交集和并集
a = set([1, 2, 3])
b = set([2, 3, 4])
print(a & b, a | b)

#%% 条件语句和循环语句，其实上面已经用到了
x = 233
# 条件语句，唯一需要注意的是冒号
if x < 0:
    y = 0
elif x < 1:
    y = 1
else:
    y = 2
# 循环语句，其中in关键字可以对所有 Iterable 的对象使用
s = [1, 2, 3]
for x in s:
    print(x)
for x in range(3):
    print(x)
n = 10
while n > 0:
    n = n - 1
print(n)
