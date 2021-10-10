'''字符串的查询操作  1.index() 查找子串substr第一次出现的位置，如果查找的子串不存在，则抛出ValueError
2.rindex() 查找子串最后一次出现的位置，如果查找的子串不存在，则抛出ValueError
find()  查找子串substr第一次出现的位置，如果查找的子串不存在,则返回-1
rfind() 查找子串最后一次出现的位置，如果查找的子串不存在，则返回-1'''
'''a='hellohello'
print(a.index('he'))   #0
print(a.rindex('he'))  #5
print(a.find('he'))    #0
print(a.rfind('he'))   #5
print(a.find('jj'))    '''#-1

'''字符串的大小写转换操作的方法  1.upper()  把字符串中所有字符都转换成大写字母
2.lower()  把字符串中所有字符都转换成小写字母   3.swapcase()   把字符串中所有小写字母都转换成大写字母，
大写字母都转换成小写字母  4. capitalize() 把第一个字符转换为大写，把其余字符转换成小写
5.title()  把每个单词的第一个字符转换成大写，把每个单词的剩余字母转换为小写'''
'''a='helloWorld,python'
#print(a.upper())  #HELLOWORLD,PYTHON
#print(id(a),id(a.upper()))          #2968513180976 2968513497408   会产生一个新的字符串对象
#print(a.lower())        #helloworld,python     会产生一个新的字符串对象
#print(a.swapcase())
print(a.title())       #Helloworld,Python
print(a.capitalize())  '''#Helloworld,python

'''字符串内容对齐操作的方法   1.center() 居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，
默认是空格，如果设置宽度小于等于实际宽度则返回原字符串  2.ljust() 左对齐，内容同上 3. rjust() 右对齐，内容同上
4.zfill() 右对齐，左边用0填充，该方法只接受一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的
宽度，则返回字符串本身'''
'''a='hello'
print(a.center(9,'*'))    #**hello**
print(a.ljust(9,"*"))     #hello****
print(a.rjust(9,'*'))     #****hello
print(a.zfill(8))         #000hello
print('-1555'.zfill(8))   '''  #-0001555

'''字符串劈分操作的方法   1.split() 从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值是一个列表
可以通过参数sep指定劈分字符串的劈分符，通过参数maxsplit指定劈分字符串的最大劈分次数，在经过最大次劈分之后，剩余的
子串会单独作为一部分   2. rsplit()  从字符串的右边开始劈分，内容同上'''
'''a='hello world python'
print(a.split())       #['hello', 'world', 'python']
b='he*llo*wo*rld'
print(b.split())           #['he*llo*wo*rld']
print(b.split(sep='*'))    #['he', 'llo', 'wo', 'rld']
print(b.split(sep='*',maxsplit=1))    #['he', 'llo*wo*rld']
print(b.rsplit(sep="*",maxsplit=1))   ''' #['he*llo*wo', 'rld']

'''判断字符串操作的方法  1. isidentifier() 判断指定的字符串是不是合法的标识符
2.isspace()  判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）
3.isalpha() 判断指定的字符串是否全部由字母组成
4. isdecimal() 判断指定字符串是否全部由十进制的数字组成
5. isnumeric() 判断指定的字符串全部由数字组成
6. isalnum() 判断指定的字符串是否全部由数字和字母组成'''
'''a='hello*'
b='hello25'
print(a.isidentifier())   #False
print(b.isidentifier())   #True
c='   '
print(c.isspace())   #True
print('abc'.isalpha())  #True
print('张三'.isalpha())  #True
print('123'.isdecimal()) #True
print('123si'.isdecimal())  #False
print('123'.isnumeric())   #True
print('123四'.isnumeric())  #True
print('123ii'.isalnum())   #True
print('123张三'.isalnum())  '''#True

'''字符串的其它操作  1.字符串替换 replace() 第一个参数指定被替换的子串，第二个指定被替换子串的字符串，该方法返回
替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大替换次数
2.字符串的合并  join() 将列表或元组中的字符串合并成一个字符串'''
'''a='helloworld'
print(a.replace('he','He'))   #Helloworld
print(a)                  #helloworld   a的字符串没有发生变化
c='hhhhh'
print(c.replace('h','k',4))     #kkkkh   h一共被替换了四次
b=['hello','java','python']
print('|'.join(b))    #hello|java|python
print(''.join(b))     #hellojavapython
print('*'.join('python'))  '''  #p*y*t*h*o*n  将python字符串作为字符串序列处理

'''字符串的比较操作  运算符： > < <= >= !=  比较原理：两个字符进行比较时，比较的是其ordinal value（原始值 ）
，调用内置函数ord可以得到指定字符的ordinal value。与内置函数ord对应的是内置函数chr，调用内置函数chr时指定
ordinal value可以得到其对应的字符
print('apple'>'app')   #True
print(ord('a'),ord('b'))   #97 98
print(chr(97),chr(98))     #a  b
print('banana'>'apple') ''' #True

''' == 与 is 的区别
== 比较的是value
is  比较的是id是否相等
a=b='python'
c='python'
print(a==b==c)   #True
print(a is b)    #True
print(b is c)    '''#True

'''字符串的切片操作  字符串是不可变类型，切片将产生新的对象  切片[start:end:step]
a='helloworld'
print(a[:5])     #hello
print(a[5:])     #world
print(a[-5::-1])  #wolleh
print(a[-5::1])   '''  #world

#格式化字符串的两种方式  1.%作占位符  %s字符串 %i或%d整数  %f 浮点数   2.{}作占位符
  #(1)   '我的名字叫做: %s,今年 %d岁了'    %    (name,age)

'''name="张三"
age=20
print('我叫%s,今年%d岁'  %  (name,age))  '''

#(2)   {}
'''name='张三'
age=21
print('我叫{0},今年{1}岁了'.format(name,age))  '''

#(3)  f-string
'''name='张三'
age=55
print(f'我叫{name},今年{age}岁了')   '''

'''print('%d' % 99)   #99
print('%5d' % 99)  #   99   5表示的是宽度
print('%.3f' % 3.14156)    #3表示的是精度，表示小数点后三位，四舍五入

print('{0:.3}'.format(3.145))   #3.15    .3表示的是一共是三位，最后一位四舍五入
print('{0:.3f}'.format(3.1456))  '''#3.146  .3f表示的是小数点后三位，最后一位四舍五入

'''字符串的编码转换  编码：将字符串转化成二进制数据  解码：将byte类型的数据转换成字符串类型'''
a='天涯共此时'
print(a.encode(encoding="GBK"))  #b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'  在GBK这种编码中，一共中文占两个字节
print(a.encode(encoding="UTF-8"))   #b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'  在UTF-8这种编码中，一个中文占三个字节


#解码
#byte代表的就是一个二进制数据   编码格式要和解码格式要相同才能正确解码
byte=a.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))     #天涯共此时