#python中的标识符和保留字
#输出python的保留字
#import keyword
#print(keyword.kwlist)

#标识符  变量、函数、类、模块和其它对象等起的名字就叫标识符
#规则 1、字母、数字、下划线 2、不能以数字开头 3、不能是保留字 4、严格区分大小写

#变量  变量由三部分组成  1，标识：表示对象所储存的内存地址，使用内置函数id(obj)来获取
#2，类型：表示的是对象的数据类型，使用内置函数type(obj)来获取
#3，值：表示对象所储存的具体数据，使用print(obj)可以将值进行打印输出
#name='hello'
#print(name)
#print('标识',id(name))
#print('类型',type(name))
#print('值',name)

#当多次赋值之后，变量名会指向新的空间

#整数可以表示为二进制、十进制、八进制、十六进制  默认输出为十进制
#print('十进制',118)  #输出118
#print('二进制',0b10101111)  #输出175  二进制以0b开头
#print('八进制',0o176)   #输出126    八进制以0o开头
#print('十六进制',0x1EAF)  #输出7855  十六进制以0x开头

#浮点类型由整数部分和小数部分组成，浮点数存储具有不精确性，使用浮点数存储时，可能会出现小数位数不确定的情况
#print(1.1+2.2)  #3.3000000000000003
#print(1.1+2.1)  #3.2

#解决方案 导入模块decimal
#from decimal import Decimal
#print(Decimal('1.1')+Decimal('2.2'))

#布尔类型 用来表示真或者假的值 True表示真，False表示假  **布尔值可以转化为整数 True->1 False->0
#print(True+1)  #2
#print(False+1) #1
#f1=False
#print(f1,type(f1))        #False <class 'bool'>

#字符串类型 可以使用单引号、双引号、三引号''' '''或者""" """来定义
#单引号和双引号定义的字符串必须在一行，三引号定义的字符串可以分布在连续的多行

#数据类型转换
name="张三"
age=20
#rint(type(name),type(age))
#print('我叫'+name+'今年,'+age+'岁') #当将str类型与int类型进行连接时，报错，解决方案，类型转换
print('我叫'+name+',今年'+str(age)+'岁') #将int类型通过str()函数转换成了str类型


'''a=10
b=10.1
c=False
#print(type(a),type(b),type(c))
print(str(a),str(b),str(c),)
print(type(str(c)))   '''  #<class 'str'>

#将别的类型的数据转换成int类型的数据
#将str转成int，字符串需要为数字串 将float转换成int类型。截取整数部分，舍掉小数部分
#如果字符串为小数串，则不能将str类型转换成int类型
'''f=1.22
print(int(f))  '''  #1  输出结果为1
#ff=True
#print(int(ff),type(int(ff)))  #输出结果为1，类型为int型

#将别的类型的数据转换成float类型的数据
'''s1='122.1'
s2='12'
s3=False
s4='hello' #字符串中的数据如果是非数字，则不允许转换
s5=45
print(float(s1),type(float(s1)))  #输出为122.1  类型为float型
print(float(s2),type(float(s2)))  #输出为12.0   类型为float型
print(float(s3),type(float(s3)))  #输出为0.0    类型为float型
print(float(s5),type(float(s5)))  '''#输出为45.0   类型为float型