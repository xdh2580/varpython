# 1
# 简介
# 简单来说函数就是一段实现特定功能的代码，使用函数可以提高代码的重复利用率。Python
# 中有很多内置函数，比如之前常用的
# print
# 函数，当内置函数不足以满足我们的需求时，我们还可以自定义函数。

# 2
# 自定义函数
# Python
# 使用
#
#
# def 关键字来声明函数，
#
#
#     格式如下所示：
#
# def 函数名(参数):
#     函数体
#     return 返回值
#

# 如果要定义一个无任何功能的空函数，函数体只写
# pass
# 即可。格式如下所示：
#
# def 函数名():
#     pass


# 当我们不确定参数的个数时，可以使用不定长参数，在参数名前加 * 进行声明，格式如下所示：
#
# def 函数名(*参数名):
#     函数体


# 我们还可以使用
# lambda 定义匿名函数，格式如下所示：
#
# lambda 参数: 表达式

# 举例：

# 空函数
def my_empty():
    pass


# 无返回值
def my_print(name):
    print('Hello', name)


# 有返回值
def my_sum(x, y):
    s = x + y
    print('s-->', s)
    return s


# 不定长参数
def my_variable(*params):
    for p in params:
        print(p)


# 匿名函数
my_sub = lambda x, y: x - y


# 3
# 函数调用
# 调用一个函数只需要知道函数名和参数即可。
#
# 举例：

my_empty()
my_print('Jhon')
result = my_sum(1, 2)
my_variable(1, 2, 3, 4, 5, 6)
print(my_sub(2, 1))
