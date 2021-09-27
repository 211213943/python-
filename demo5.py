#pass语句   pass语句什么都不做，只是一个占位符，用在语法上需要语句的地方
#什么时候使用，先搭建语法结构，还没想好代码怎么写的时候

#内置函数range()  用于生成一个整数队列
#创建range函数的三种方式   1.range(stop) 创建一个[0,stop)之间的整数序列，步长为1
#2.range(start,stop)  创建一个[start,stop)之间的整数序列，步长为1
#3.range(start,stop,step) 创建一个[start,stop)之间的整数序列，步长为step
#返回值是一个迭代器对象
#第一种创建方式
'''r=range(10)    #默认从0开始，默认相差1称为步长
print(r)      #range(0, 10)
print(type(r))         # <class 'range'>
print(list(r))   '''#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  用于查看range对象中的整数队列   '''

'''第二种创建方式
r=range(1,10)
print(list(r))       输出结果[1, 2, 3, 4, 5, 6, 7, 8, 9]   '''

'''第三种创建方式
r=range(1,10,2)
print(list(r))   输出结果[1, 3, 5, 7, 9]    '''

'''判断指定的整数 在序列中是否存在使用  in  not in
r=range(1,10,2)
print(10 in r)  #False 10不在指定的序列中  '''


#print(list(range(1,10)))   [1, 2, 3, 4, 5, 6, 7, 8, 9]