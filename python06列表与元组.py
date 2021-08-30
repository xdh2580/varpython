# 1 列表
# 1.1 简介
# Python 中没有数组，而是加入了功能更强大的列表（list），列表可以存储任何类型的数据，同一个列表中的数据类型还可以不同；列表是序列结构，可以进行序列结构的基本操作：索引、切片、加、乘、检查成员。

# 1.2 基本使用
# ➢ 创建
#
# 列表中所有元素都放在一个中括号 [] 中，相邻元素之间用逗号 , 分隔，如下所示：

l = [1024, 0.5, 'Python']
# ➢ 访问
#
# 通过索引访问列表中的值，还可以使用 : 截取范围内的元素，如下所示：

l = [1024, 0.5, 'Python']
print('l[0] -->', l[0])
print('l[1:] -->', l[1:])
# 输出结果：
#
# l[0] --> 1024
# l[1:] --> [0.5, 'Python']
# ➢ 更新

# 除了对列表中现有元素进行修改外，还可以使用 append() 向列表中添加新元素，如下所示：

l = [1024, 0.5, 'Python']
# 修改列表中第二个元素
l[1] = 5
# 向列表中添加新元素
l.append('Hello')
print('l[1] -->', l[1])
print('l -->', l)
# 输出结果：
#
# l[1] --> 5
# l --> [1024, 5, 'Python', 'Hello']
# ➢ 删除
#
# 使用 del 删除列表中元素，如下所示：

l = [1024, 0.5, 'Python']
# 删除列表中第二个元素
del l[1]
print('l -->', l)
# 输出结果：
#
# l --> [1024, 'Python']
# ➢ 常用方法
#
# ① count()
#
# 统计列表中某个元素出现的次数，使用如下所示：

l = ['d', 'b', 'a', 'f', 'd']
print("l.count('d') -->", l.count('d'))
# 输出结果：
#
# l.count('d') --> 2
# ② index()

# 查找某个元素在列表中首次出现的位置（即索引），使用如下所示：

l = ['d', 'b', 'a', 'f', 'd']
print("l.index('d') -->", l.index('d'))
# 输出结果：
#
# l.index('d') --> 0
# ③ remove()

# 移除列表中某个值的首次匹配项，使用如下所示：

l = ['d', 'b', 'a', 'f', 'd']
l.remove('d')
print("l -->", l)
# 输出结果：
#
# l --> ['b', 'a', 'f', 'd']
# ④ sort()

# 对列表中元素进行排序，使用如下所示：

l = ['d', 'b', 'a', 'f', 'd']
l.sort()
print('l -->', l)
# 输出结果：
#
# l --> ['a', 'b', 'd', 'd', 'f']
# ⑤ copy()
#
# 复制列表，使用如下所示：

l = ['d', 'b', 'a', 'f', 'd']
lc = l.copy()
print('lc -->', lc)
# 输出结果：
#
# lc --> ['d', 'b', 'a', 'f', 'd']


# 2 元组
# 2.1 简介
# 元组（tuple）与列表类似，但元组是不可变的，可简单将其看作是不可变的列表，元组常用于保存不可修改的内容。
#
# 2.2 基本使用
# ➢ 创建
#
# 元组中所有元素都放在一个小括号 () 中，相邻元素之间用逗号 , 分隔，如下所示：

t = (1024, 0.5, 'Python')
# ➢ 访问
#
# 与访问列表中元素类似，如下所示：

t = (1024, 0.5, 'Python')
print('t[0] -->', t[0])
print('t[1:] -->', t[1:])
# 输出结果：
#
# t[0] --> 1024
# t[1:] --> (0.5, 'Python')
# ➢ 修改

# 元组中元素不能被修改，我们要用重新赋值的方式操作，如下所示：

t = (1024, 0.5, 'Python')
t = (1024, 0.5, 'Python', 'Hello')
print('t -->', t)
# 输出结果：
#
# t --> (1024, 0.5, 'Python', 'Hello')
# ➢ 删除

# 元组中的元素不能被删除，我们只能删除整个元组，如下所示：
#
# t = (1024, 0.5, 'Python')
# del t
# print('t -->', t)
# 输出结果：
#
# NameError: name 't' is not defined
#
# 由于元组实例被删除，所以输出了异常信息。
#
# ➢ 常用方法
#
# ① len()
#
# 计算元组中元素个数，使用如下所示：

t = (1024, 0.5, 'Python')
print('len(t) -->', len(t))
# 输出结果：
#
# len(t) --> 3
# ② max() 和 min()

# 返回元组中元素最大、最小值，使用如下所示：

t = ('d', 'b', 'a', 'f', 'd')
print('max(t) -->', max(t))
print('min(t) -->', min(t))
# 输出结果：
#
# max(t) --> f
# min(t) --> a
# ③ tuple()

# 将列表转换为元组，使用如下所示：

l = ['d', 'b', 'a', 'f', 'd']
t = tuple(l)
print('t -->', t)
# 输出结果：
#
# t --> ('d', 'b', 'a', 'f', 'd')
