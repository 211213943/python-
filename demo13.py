'''字符串是python的基本数据类型，是一个不可变的字符序列
  字符串的驻留机制，即仅保留一份相同且不可变字符串的方式，不同的值被存放在字符串的驻留池中，python的驻留机制
  对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量
s='python'
a="python"   '''
#b='''python'''
#print(id(a),id(b),id(s))       #三者的地址相同
'''字符串驻留的集中情况  1.字符串的长度为0或者1时  2.符合标识符的字符串  3.字符串只在编译时进行驻留，而非运行时
4. [-5,256]之间的整数数字    pycharm对驻留机制进行了优化'''

'''s1=''
s2=''
print(s1 is s2)   '''  #True

'''s1='adc%'
s2='adc%'
print(s1 is s2)
print(id(s1),id(s2))   '''   #id值相同，这是pycharm对驻留机制进行了优化

'''a='abc'
b='a'+'bc'
c=''.join(['ab','c'])
print(a is b)     #True
print(a is c)     ''' #False

'''a=-5
b=-5
print(a is b)      #True
c=-6
d=-6
print(c is d)   '''   #True  pycharm对驻留机制进行了优化