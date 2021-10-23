'''python中的包，包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
包的作用：代码规范  避免模块起冲突
包与目录的区别： 1.包含_init_.py文件的目录称为包   2.目录中通常不包含_init_.py文件
目录：directory
包的导入     import 包名.模块名称
导入带有包的模块时的注意事项
使用import方式导入时，只能跟包名或者模块名
使用from...import可以导入包、模块、函数、变量等'''

#python中常用的内容模块
'''import sys  #与python解释器及环境操作相关的标准库
print(sys.getsizeof(1))  #获取整数所占的内存大小
print(sys.getsizeof(1.0))
import time  #提供与时间相关的各种函数的标准库
print(time.time())
print(time.localtime(time.time())) '''

#import os       提供了访问操作系统服务功能的标准库
#import calendar   #提供了与日期相关的各种函数的标准库
'''import urllib.request   #用于读取来自网上（服务器）的标准数据库,爬虫的时候会用到
print(urllib.request.urlopen('http://www.baidu.com').read())   '''
#import json  用于使用JSON序列化和反序列化对象
#import re  用于在字符串中执行正则表达式匹配和替换
#import decimal 用于进行精确控制运算精度、有效位数和四舍五入的十进制运算
#import logging  提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能

#第三方模块的安装
#pip  install  模块名   例  pip  install  schedule
#第三方模块的使用          import 模块名
'''import schedule
import time
def job():
    print('hahahaha')
schedule.every(1).seconds.do(job)  #每隔三秒执行job函数
while True:
    schedule.run_pending()
    time.sleep(1)   '''#休眠一秒
