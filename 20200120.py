# -*- coding: UTF-8 -*-

# Filename: 20200120.py
# Author: yangtonggang

"""
#实例：求和

#用户输入数字
num1 = input('输入第一个数字')
num2 = input('输入第二个数字')

#求和
sum = float(num1) + float(num2)

#显示计算结果
print('数字{0}+数字{1}，结果={2}'.format(num1, num2, sum))

#合并为一行代码的写法
print('两数之和为%.1f' %(float(input('输入第一个数字'))+float(input('输入第二个数字'))))
"""

'''
num = float(input('输入一个数字：'))
num_sqrt = num ** 0.5
print('%.3f 的平方根是 %.3f' %(num, num_sqrt))
'''

'''
import random
print(random.randint(0, 9))

x = 1
y = 2

#x,y = y, x

#x=y
#y=x

x = x + y
y = x - y
x = x - y

print('x是%d, y是%d' %(x, y))
print('x是{}; y是{}'.format(x, y))
'''

'''
num = int(input("请输入一个整数: "))
if (num % 2) == 0:
   print("{} 是偶数".format(num))
else:
   print("{} 是奇数".format(num))

'''

'''
import calendar
year = int(input('输入年份'))
check_year = calendar.isleap(year)
if check_year == True:
    print('是闰年')
else:
    print('不是闰年')
'''

'''
# 用户输入数字
num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")
'''


