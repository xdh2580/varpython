# 1 字典
# 1.1 简介
# dict 拥有良好的查询速度，dict 中的值可以是任意 Python 对象，多次对一个 key 赋 value，后面的 value 会把前面的 value 覆盖。
#
# 1.2 使用
# 字典的内容在花括号 {} 内，键-值（key-value）之间用冒号 : 分隔，键值对之间用逗号 , 分隔，比如创建字典 d，如下所示：

d = {'name': '小明', 'age': '18'}

# 使用 dict 函数
# 方式一
l = [('name', '小明'), ('age', 18)]
d = dict(l)
# 方式二
d = dict(name='小明', age='18')

# 空字典
d = dict()
d = {}
# 字典中的值通过 key 进行访问，如下所示：
#
# >>> d = dict(name='小明', age='18')
# >>> d['name']
# '小明'

# 使用 get 方法
# >>> d.get('name')
# '小明'
# 修改操作，以修改 age 为例，如下所示：
#
# >>> d = dict(name='小明', age='18')
# >>> d['age'] = '20'
# >>> d['age']
# '20'
# 清空集合，如下所示：

# >>> d = dict(name='小明', age='18')
# >>> d.clear()
# >>> d
# {}
# 获取字典的长度，如下所示：
#
# >>> d = dict(name='小明', age='18')
# >>> len(d)

'''
2
2 集合
2.1 简介
集合（set）与字典相同均存储 key，但也只存储 key，因 key 不可重复，所以 set 的中的值不可重复，也是无序的。

2.2 使用
集合使用花括号 {} 或者 set() 函数创建，如果创建空集合只能使用 set() 函数，以创建集合 s 为例，如下所示：

s = {'a', 'b', 'c'}

使用 set 函数
s = set(['a', 'b', 'c'])

空集合
s = set()
集合中重复的元素会被自动过滤掉，如下所示：

>>> s = {'a', 'a', 'b', 'c', 'c'}
>>> s
{'a', 'c', 'b'}
添加元素可以使用 add 或 update 方法，如果元素已经存在，则不进行操作，如下所示：

>>> s = {'a', 'b', 'c'}
>>> s.add('d')
>>> s
{'a', 'd', 'c', 'b'}
>>> s.update('e')
>>> s
{'a', 'b', 'e', 'd', 'c'}
# 添加已经存在的元素 a
>>> s.add('a')
>>> s
{'a', 'b', 'e', 'd', 'c'}
删除元素使用 remove 方法，如下所示：

>>> s = {'a', 'b', 'c'}
>>> s.remove('c')
>>> s
{'a', 'b'}
清空集合使用 clear 方法，如下所示：

>>> s = {'a', 'b', 'c'}
>>> s.clear()
>>> s
set()
获取集合的长度，同样使用 len 方法，如下所示：

>>> s = {'a', 'b', 'c'}
>>> len(s)
3
'''
s = {'a', 'b', 'a', 'c'}
print(len(s))
