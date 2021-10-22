'''一个模块（Modules）中可以包含N多个函数，在python中一个扩展名为.py的文件就是一个模块,如demo1.py就是一个模块
使用模块的好处  1.方便其它程序和脚本的导入并使用   2.避免函数名与变量名冲突  3.提高代码的可维护性  4.提高代码的可重用性'''
#创建模块  新建一个.py的文件，名称尽量不要与python自带的标准模块名称相同
'''导入模块    import 模块名称  [as 模块别名]
              from    模块名称  import  函数/变量/类
            '''
#(1)导入整个math模块
'''
import  math
print(id(math))
print(type(math))
print(math.pi)
print('====================')
print(dir(math))
print(math.cos(0))
print(math.pow(2,3))  #8.0   类型为float
print(math.ceil(7.00001))    #8
print(math.floor(8.0001))  ''' #8

#(2) 导入math模块中指定的内容
'''from  math import  pi
print(pi)      # 3.141592653589793
from  math import  pow
print(pow(2,3))  ''' #8.0


#在demo25中导入calc自定义模块
import  calc
print(calc.add(10,20))
print(calc.mul(10,20))