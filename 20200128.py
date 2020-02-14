# -*- conding: utf-8 -*-
# Author: yangtonggang
# Filename: 20200128.py

import logging

#字符串是否存在子字符串
def check(str, sub_str):
    if (str.find(sub_str)==-1):
        print('不存在！')
    else:
        print('存在！')
str = 'www.runoob.com'
sub_str = 'runoob'
check(str, sub_str)
logging.info(str)


'''
import re

def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url
string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("Urls1: ", Find(string))
print("Urls2: ", re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string))
'''

'''
def exec_code():
    LOC = """
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i  #1*1 1*2 2*3 6*4 24*5
    return fact
print(factorial(5))
"""
    exec(LOC)
exec_code()


str='Runoob'

print(str[::-1])
print(''.join(reversed(str)))
print(''.join(reversed('Runoob')))
'''

'''
def dictionairy():
    key_value={}

    key_value[2]=56
    key_value[1]=20
    key_value[5]=12
    key_value[4]=24
    key_value[6]=18
    key_value[3]=323

    print('按值排序')
    print(sorted(key_value.items(), key=lambda kv:(kv[1], kv[0])))

def main():
    dictionairy()

if __name__ == "__main__":
    main()
'''

'''
lis = [{'name':'taobao', 'age':100},
{'name':'runoob', 'age':7},
{'name':'google', 'age':100},
{'name':'wiki', 'age':200}]

print('列表通过age升序排序')
print(sorted(lis, key=lambda i:i['age']))

print('\r')

print('列表通过age和name排序')
print(sorted(lis, key=lambda i:(i['age'], i['name'])))

print('\r')

print('列表通过age降序排序')
print(sorted(lis, key=lambda i:i['age'], reverse=True))
'''

'''
def returnjieguo(jisuan):
    sum=0
    for i in jisuan:
        sum=sum+jisuan[i]
    return sum

str1 = {'ab':100, 'cd':200, 'ef':300}
print(returnjieguo(str1))
'''

'''
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
print("字典移除前 : ", test_dict)
print("字典移除前 : " + str(test_dict))
print("字典移除前 : ", str(test_dict))

del test_dict["Zhihu"]
print("字典移除4后 :" + str(test_dict))

test_dict.pop('Taobao')
print("字典移除3后 :", test_dict)

new_test_dict = {key : val for key, val in test_dict.items() if key != 'Google'}
print('字典移除2后：', new_test_dict)
'''

'''
def Merge(dict1, dict2):
    return (dict1.update(dict2))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(Merge(dict1, dict2))
print(dict1)
'''

'''
def merge(dic1, dic2):
    res = {**dic1, **dic2}
    return res

dicc1 = {'a': 10, 'b': 8}
dicc2 = {'d': 6, 'c': 4}
dicc3 = merge(dicc1, dicc2)
print(dicc3)
'''

'''
import time
import datetime

ai="2020-1-12 12:12:3"

#字符串转换为时间数组
timeArray=time.strptime(ai, "%Y-%m-%d %H:%M:%S")
print(timeArray)

#时间数组转换为时间格式
otherTime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherTime)

#时间数组转换为时间戳
timeStamp=int(time.mktime(timeArray))
print(timeStamp)

#时间戳转换为时间格式
dateArray=datetime.datetime.utcfromtimestamp(timeStamp)
print(dateArray)


threeDayAgo=dateArray-datetime.timedelta(days=3)
print(threeDayAgo)

print('-----------------------')

# 获得当前时间时间戳
now = int(time.time())
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
#时间数组转换为时间格式
otherStyleTime1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime1)

# 获得当前时间*******
now = datetime.datetime.now()
# 转换为指定的时间格式******
otherStyleTime2 = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime2)

#优化的常用版本******
import datetime
now=datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
'''

'''
# Python 字典类型转换为 JSON 对象
import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str1 = json.dumps(data)    #编码
json_str2 = json.loads(json_str1)   #解码

print("Python 原始数据：", data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str1)
print("JSON解码后 Python 原始数据：", json_str2)
'''

'''
import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data1 = json.load(f)

print(data1)
'''