def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
# fun(10,20,30)   #函数调用时的位置参数，称为位置传参
lst=[11,22,33]
#*args 代表可接受列表或者元组作为参数，可以用 * 解包列表或者元组作为位置参数
# fun(*lst)  #在函数调用时，将列表中的每个元素都转换为位置实参传入
# fun(a=100,b=2,c=22)  #函数的调用，是关键字实参
dic={'c':100,'a':2,'b':22}
#**args 代表可以接受字典作为函数的参数传入，可以用 ** 解包字典为关键字参数
fun(**dic)    #在函数调用时，将字典中的每个键值对都转换成关键字实参,字典中的key要和函数中的形参相对应

'''def fun(a,b=10):
    print('a=',a)
    print('b=',b)

def fun1(*args):
    print(args)  #个数可变的位置形参

def fun2(**args):
    print(args)  #个数可变的关键字形参
fun1(10,20)
fun2(a=11,b=111)

def fun3(a,b,c,d,):
    print('a=',a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
fun3(10,20,30,40)
fun3(a=10,b=20,c=30,d=40)
fun3(10,20,c=30,d=40)   #前两个参数采用的是位置实参传递，后两个参数采用的是关键字实参传递

''''''需求 c和d只能采用关键字实参传递'''
'''def fun4(a,b,*,c,d,):   #从*之后的参数，在函数调用时，只能采用关键字实参传递
    print('a=',a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
#fun4(10,20,30,40)     运行会报错，因为c和d没有采用关键字实参传递
fun4(a=10,b=20,c=30,d=40)
fun4(10,20,c=30,d=40)   #前两个参数采用的是位置实参传递，后两个参数采用的是关键字实参传递

# 函数定义时的形参的顺序问题
def  fun5(a,b,*,c,d,**args):
    pass

def fun6(*args,**args1):
    pass

def fun7(a,b=10,*args1,**args2):
    pass '''


