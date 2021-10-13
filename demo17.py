'''变量的作用域：程序代码能够访问该变量的区域  1.局部变量，在函数内定义并使用的变量，只在函数内部有效，局部变量
使用global声明，这个变量就会变成全局变量   2.全局变量：函数体外定义的变量，可作用于函数内外'''
'''def  fun():
    global age
    age=20
    print(age)
fun()
print(age)    '''

'''递归函数，如果一个函数的函数体内调用了该函数本身，这个函数就称为递归函数'''
'''def fun(n):    #使用递归计算阶乘
    if n==1:
        return 1
    else:
        return n*fun(n-1)
print(fun(5))   '''

'''斐波那契数列'''
def fun(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)
print(fun(3))         #返回斐波那契数列第三位上的数字

'''输出斐波那契数列前六位的数字'''
for i  in  range(1,7):
    print(fun(i))