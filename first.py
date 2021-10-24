# python的单行注释用的是#键
#python中的print()函数,可以直接使用,可以输出数字，也可以输出字符串
#print(520)
#print("helloworld")  #输出字符串

#可以输出含有运算符的表达式,会计算表达式的结果并将计算后的结果输出
#print(3+1)


#可以将数据输出到文件当中  注意点， 1 所指定的盘符要存在  2 使用file=的格式
#fp=open('D:/text.txt','a+') #a+如果文件不存在就创建，存在就在文件内容的后面继续追加
#print('helloworld',file=fp)
#fp.close()

#不进行换行输出（即输出内容在一行） 使用逗号进行分割
#print('hello','world','python')


#转义字符
#print('hello\nworld')  #\ +转义功能的首字母  n-->newline的首字母表示换行
#print('hello\rworld')  #只会输出world  \r回车功能使得hello被world给覆盖掉了
#print('hello\bworld')  # 输出hellworld  \b是退一个格。将o给退没了

#当字符串中包含反斜杠、单引号和双引号等有特殊用途的字符时，必须使用反斜杠对这些字符进行转义
print('他说：\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或者R
#注意事项 最后一个字符不能是一个反斜杆，否则会报错
#print(r'hello\nworld')  #转义字符没有起作用
print('hello\nworld')  #转义字符起作用了
#print(r'hello\nworld\')   会报错