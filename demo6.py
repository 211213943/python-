#循环结构 循环的分类 while  for-in
'''while 条件表达式:
      条件执行体（循环体）   '''
'''a=1
while  a<10:
    print(a)
    a+=1    '''

'''for-in 循环 in表达从（字符串，序列等）中依次取值，又称为遍历
for-in 遍历的对象必须是可迭代对象
for-in的语法结构

for 自定义的变量  in 可迭代对象:
               循环体
循环体内不需要访问自定义变量时，可以将自定义变量替代为下划线
'''
#for item in 'python':  依次将'python'赋值给item对象
#  print(item)

#range()产生一个整数序列，也是一个可迭代对象
'''for  i in range(10):
    print(i)       '''

#如果在循环体中不需要使用到自定义变量，可以将自定义变量写为"_"
for  _  in range(5):
    print("人生苦短，我用python")

#输出100到999之间的水仙数   水仙花数举例  153=3*3*3+5*5*5+1*1*1
'''for  item in range(100,1000):
    ge=item%10   #个位上的数
    shi=item//10%10   #十位上的数
    bai=item//100     #百位上的数
    if ge**3+shi**3+bai**3==item:
        print(item)'''
