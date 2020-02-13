total = ['item_one', 'item_two', 'item_three', 'item_four', 'item_five']
print(len(total))

str1 = '联系'
print(str1)
print(str1 + "您好")

import sys
x = 'runoob'
sys.stdout.write(x + '\n')

x="a"
y="b"
print(x, end=".")


def a():
    '''这是注释'''
    pass
print(a.__doc__)


languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

var2 = 10
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)

'''
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")
'''

list = [1, 2, 3, 4, 5]
it = iter(list)
print(next(it))
print(next(it))
print(list[1])

a = [66.25, 333, 333, 1, 1234.5]
print(a)
a.pop()
print(a)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon for weapon in freshfruit])
for weapon in freshfruit:
    print(weapon, end=" ")

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
