'''
dir(pickle)
help(pickle)
'''

'''
import pickle, pprint

data1 = {'a':[1, 2.0, 3, 4+6j], 'b':('string', u'Unicode string'), 'c':None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
print('selfref:', selfref_list)

output = open('d:\\data.pkl', 'wb')

pickle.dump(data1, output)
print('1:', output)

pickle.dump(selfref_list, output, -1)
print('2:', output)

output.close()



pkl_file = open('d:\\data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)
print(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)
print(data2)

pkl_file.close()

'''

'''
print(next.__module__)

# 打开文件
fo = open("d:\\runoob.txt", "r+")
print ("文件名: ", fo.name)

str = "6:www.runoob.com"
# 在文件末尾写入一行
fo.seek(0, 2)
line = fo.write(str)

# 读取文件所有内容
fo.seek(0,0)
for index in range(6):
    line = next(fo)
    print ("文件行号 %d - %s" % (index, line))

# 关闭文件
fo.close()

'''

'''
while True:                                                
    try:                                                   
        x = int(input("请输入一个数字: "))                       
        break                                              
    except ValueError:                                     
        print("您输入的不是数字，请再次尝试输入！")                         
'''

'''
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
'''

'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
'''

'''
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
'''

'''
with open("d:\\runoob.txt") as f:
    for line in f:
        print(line, end="")
'''

"""
import os,sys,glob

print(os.getcwd())
print(os.system('cd..'))
print(dir(os))
print(sys.argv)
print(glob.glob('*.py'))
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.stdout.write('标准输出')
"""

'''
from datetime import date

now = date.today()
print(now.strftime("%y-%m-%d, %d %b %Y is a %A on the %d day of %B."))
print(now.strftime('%Y-%m-%d, %d is %B %A'))

birthday = date(1976, 7, 6)
age = now-birthday
print(age.days)

from timeit import Timer

print('1:', Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print('2:', Timer('a,b = b,a', 'a=1; b=2').timeit())
'''

'''
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest, unittest

print(doctest.testmod())   # 自动验证嵌入测试


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests
'''

'''
from urllib.request import urlopen
from urllib.parse import urlencode

url='http://www.xxx.com/login'
data={"username":"admin", "password":123456}
req_data=urlencode(data) #将字典类型的请求数据转变为url编码
res=urlopen(url+'?'+req_data) #通过urlopen方法访问拼接好的url
print(res)
res=res.read().decode() #read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
print(res)


#处理post请求,如果传了data，则为post请求
from urllib.request import Request
from urllib.parse import urlencode

url='http://www.xxx.com/login'
data={"username":"admin","password":123456}
data=urlencode(data)#将字典类型的请求数据转变为url编码
data=data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
req_data=Request(url,data)#将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
    res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)
'''
