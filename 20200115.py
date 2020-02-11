import sys
"""
print('命令行参数如下:\n')
for i in sys.argv:
    print('脚本路径为', i)
print('\nPython 路径为：', sys.path, '\n')
"""

"""
print('sys模块内定义的所有名称：', dir(sys))

s = 'abcdefg'
print('str打印s的内容：', str(s))
print('repr打印s的内容：', repr(s))

hello = 'hello\n'
print(repr(hello))
print(hello)
print('打印repr_doc内容：', repr.__doc__, '\n----------------', '\n打印rjust内容:', repr(hello).rjust(10))
print('打印ljust、zfill内容：', repr(hello).ljust(10), repr(hello).zfill(20))
print('{1}：{0}!'.format( '今天好', '明天好'))

import math
print(dir(math), '\n', math.pi, 'acos的dco是', math.pi.__doc__)
print('常量 PI 的值近似为：{0:.5f}。'.format(math.pi))
print('常量 PI 的值近似为：%.5f。' % math.pi)
"""

'''
# 打开一个文件
f = open(r"d:\gang.txt", "a")
f.write( "Python 重新写入行吗。\n是的，的确非常好重新写入!!\n" )
# 关闭打开的文件"
f.close()

import io
f = open(r"d:\gang.txt", "r")
word = f.read()
print(word)
f.close()
dir(io)
help(io)
'''

"""
python的标准库中文文档地址：https://docs.python.org/zh-cn/3/
"""

s = str('abcdefg')
print(str.capitalize(s))
print(open.__module__)

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('12'.zfill(5))
print('12'.ljust(5))
print('12'.center(5))

table = {'one':1, 'two':2, 'three':3}
for name, number in table.items():
    print('{0:5} ==> {1:10d}'.format(name, number))