'''函数就是执行特定任务以完成特定功能的一段代码
函数的创建      def  函数名([输入参数]) :
                        函数体
                        [return xxx]'''
def  calc(a,b):
    c=a+b
    return c
'''result=calc(20,20)   位置实参
print(result)  '''
'''result=calc(b=1,a=5)    关键字参数传递
print(result)  '''

#函数的参数传递   1.位置实参，根据形参对应的位置进行实参传递  2.关键字传递，根据形参名称进行实参传递
#在函数调用过程中，进行参数的传递，如果是不可变对象，在函数体的修改不会影响实参的值
#如果是可变对象，在函数体内的修改会影响实参的值
'''个数可变的位置参数（只能定义一个）  定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数，使用
*定义个数可变的位置形参，输出结果为一个元组'''
'''def fun(*args):
    print(args)
fun(10)        #(10,)
fun(10,20)  '''   #(10, 20)

'''个数可变的关键字形参（只能有一个）
定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字形参，使用**定义个数可变的关键字形参
结果为一个字典'''
'''def  fun(**args):
    print(args)
fun(a=10)        #{'a': 10}
fun(a=0,b=100)    '''#{'a': 0, 'b': 100}
#函数返回多个值时，结果为元组
'''def fun(num):
    jishu=[]
    oushu=[]
    for i in num:
        if i%2:
            jishu.append(i)
        else:
            oushu.append(i)
    return jishu,oushu
print(fun([20,45,55,40]))    '''#([45, 55], [20, 40])
'''函数的返回值   函数在定义时，是否需要返回值，视情况而定
（1）如果函数没有返回值【函数执行完不需要给调用处提供数据】 return可以省略不写
（2）函数的返回值，如果是一个，直接返回原类型
（3）函数的返回值是多个，返回的结果为元组'''

'''函数的参数定义  函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参'''
'''def fun(a,b=10):
    print(a,b)
fun(100)   #只传递一个参数，b采用默认值
fun(10,100)  #100将b的默认值10替换   '''

'''print()   #跳转到该函数的源码处，可以选中该函数然后按Ctrl+b进行跳转
print('hello',end='\t')
print('world')    ''' #hello	world