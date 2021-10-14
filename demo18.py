#python的异常处理机制，可以在异常出现时及时捕获
'''try:
    n1=int(input('请输入第一个整数'))   #可能会出现错误的代码
    n2=int(input('请输入第二个整数'))
    res=n1/n2
    print('结果为',res)
except ZeroDivisionError:
    print('除数不能为0哦')
except ValueError:
    print('只能输入数字串')  '''

#try...except...else结构  如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
'''try:
    n1=int(input('请输入第一个整数'))
    n2=int(input('请输入第二个整数'))
    res=n1/n2
except BaseException as e:   #将错误起个别名e
    print('出错了')
    print(e)
else:
    print('结果为:',res)     '''

#try....except...else..finally结构，finally块无论是否发生异常都会被执行，常用来释放try块中申请的资源
'''try:
    n1=int(input('请输入第一个整数'))
    n2=int(input('请输入第二个整数'))
    res=n1/n2
except BaseException as e:   #将错误起个别名e
    print('出错了')
    print(e)
else:
    print('结果为:',res) 
finally:
    print('无论是否产生异常，总会被执行的代码') 
'''

#常见类型的错误
#print(10/0)        # ZeroDivisionError
'''lst=[11,22]
#print(lst[2])        #IndexError
dic={'name':'张三','age':20}
#print(dic['gender'])      #KeyError
#print(num)        #NameError: name 'num' is not defined
#int a=20        #SyntaxError: invalid syntax
print(int('nane'))   ''' #ValueError: invalid literal for int() with base 10: 'nane'

'''使用traceback模块打印异常信息
import traceback
try:
    print('----------')
    print(1/0)
except:
    traceback.print_exc()    '''