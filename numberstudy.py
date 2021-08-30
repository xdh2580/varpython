import math
# 1 数值类型
# 我有三种数值类型，分别是：整型（int）、浮点型（float）、复数（complex），如果你使用的还是我的低版本 Python2，那么还包含长整型（long）。
#
# 整型：包括正整数、负整数。如：1024、-1024。整型有四种进制表示，分别为：二进制、八进制、十进制、十六进制，说明如下表所示：
# 种类	描述	引导符
# 二进制	由 0 和 1 组成	0b 或 0B
# 八进制	由 0 到 7 组成	0o 或 0O
# 十进制	默认情况	无
# 十六进制	由 0 到 9、a 到 f、A 到 F 组成，不区分大小写	0x 或 0X
# 浮点型：由整数部分和小数部分组成。
#
# 复数：由实数部分和虚数部分组成。
a = 0b1010
b = 6
print(a+b)
#2 基本运算
# 运算	描述
# x + y	x 和 y 的和
# x - y	x 和 y 的差
# x * y	x 和 y 的乘积
# x / y	x 和 y 的商
# x // y	x 除以 y，取整除
# x % y	x 除以 y，取模
# -x	x 取反
# +x	x 不变
# abs(x)	x 的绝对值
# int(x)	将 x 转换为整数
# float(x)	将 x 转换为浮点数
# complex(x, y)	一个带有实部 x 和虚部 y 的复数，y 默认为 0。
# divmod(x, y)	(x // y, x % y)
# pow(x, y)	x 的 y 次幂
# x ** y	x 的 y 次幂
x = "62"
a = int(x)
print(a)

# 3 数学函数
# 除了上面的基本运算外，我还可以借助数学模块 math 实现更多的运算。
#
# 首先要先引入数学模块 math。如下所示：
#
# import math
# 引入之后就可以使用了，以 math 模块中求平方根函数 sqrt(x)  为例。使用方式如下所示：
#
# import math
# math.sqrt(1024)
# math 模块中除了求平方根函数，还有很多可以使用的函数。如下表所示：
#
# 函数	描述
# abs(x)	返回 x 的绝对值
# ceil(x)	返回 x 的上入整数，如：math.ceil(1.1) 返回 2
# floor(x)	返回 x 的下舍整数，如：math.floor(1.1) 返回 1
# exp(x)	返回 e 的 x 次幂
# log(x)	返回以 e 为底 x 的对数
# log10(x)	返回以 10 为底 x 的对数
# pow(x, y)	返回 x 的 y 次幂
# sqrt(x)	返回 x 的平方根
# factorial(x)	返回 x 的阶乘

# 4 随机函数
# 在安全领域有时会用到随机数，random 模块对随机数的生成提供了支持。
#
# 首先还是要引入 random 模块。如下所示：
#
# import random
# 下面简单介绍两个函数：
#
# random(x)函数
#
# 随机生成一个 0 到 1 范围内的实数。使用如下所示：
#
# import random
# random.random()
# uniform(x, y)函数
#
# 随机生成一个 x 到 y 范围内的实数。使用如下所示：
#
# import random
# random.uniform(1,10)