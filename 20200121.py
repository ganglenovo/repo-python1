# -*- coding: UTF-8 -*-

# Author: yangtonggang
# Filename: 20200121/py

'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata  # 处理ASCii码的包
        for i in s:  #教程代码当出现多个汉字数字时会报错，通过遍历字符串解决
            unicodedata.numeric(i)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试字符串和数字
print(is_number('1'))  # True
print(is_number('1.3'))  # True
print(is_number('-1.37'))  # True
print(is_number('1e3'))  # True
print(is_number('foo'), '\n')  # False

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四'))  # True
# 版权号
print(is_number('©'))  # False
'''

'''
# 通过用户输入数字计算阶乘

# 获取用户输入的数字
num = int(input("请输入一个数字: "))
factorial = 1

# 查看数字是负数，0 或 正数
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
        #print(factorial)
    print("%d 的阶乘为 %d" % (num, factorial))
'''

'''
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print('')
'''

'''
list1 = [10, 20, 4, 45, 99]

list1.sort()

print("最小元素为:", list1[0])
print("最大元素为:", *list1[:1])
'''



