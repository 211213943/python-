#python中的运算符
#常用运算符 1，算数运算符 （1.1，标准算数运算符 1.2，取余运算符 1.3，幂运算符）
# 2，赋值运算符 3，比较运算符 4，布尔运算符 5，位运算符
#print(1+1) #执行加法运算
print(1/2) #除法运算 结果为0.5
print(type(1/2))     #<class 'float'>
#print(11//2) #整除运算，结果为5
#print(11%2)  #取余运算
#print(2**2)  #幂运算，表示2的2次方
#print(2**3)  #幂运算，表示2的3次方

#print(-9//-4) #结果为2
#print(-9//4)  #结果为-3   一正一负时向下取整

#print(-9%4)  #结果为3  一正一负取余要遵循公式  公式为 余数=被除数-除数*(二者整除的值)
#print(9%-4)  #结果为-3


#赋值运算符，预算顺序从右到左,支持链式赋值，参数赋值以及系列解包赋值
'''a=b=c=20  #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))''' #三者的id均相同

# a,b,c=20,30,40   系列解包赋值
#交换两个变量的值
#a,b=10,20
#print("交换之前",a,b)
#a,b=b,a    #两个变量的交换不需要中间变量
#print("交换之后",a,b)

#比较运算符 对变量或表达式的结果进行大小、真假等比较  比较运算符的结果类型为bool类型
#a,b=10,20
#print('a>b吗？',a>b)  #False

# ==比较的是两个对象的值  比较对象的标识使用的是is
#a=10
#b=10
#print(a==b)  #True  a与b的值相同
#print(a is b) #True a与b的id标识也相同

'''lst1=[11,22]
lst2=[11,22]
print(lst1==lst2)  #True
print(lst1 is lst2) #False
print(id(lst1))
print(id(lst2))
print(lst1 is not lst2)  #True 两个id不相同  '''

#布尔运算符
#not 如果运算数为True,运算结果为False 如果运算数为False，运算结果为True
#f=True
#print(not f)  #False

#in  not in运算符
#s="helloworld"
#print('l' in s)  #True
#print('s' in s)  #False

#位运算符 将数据转换成二进制进行计算
#print(4&8)  #0 按位与运算   对应数位都是1，结果数位才是1，否则为0
#print(4|8)  #12 按位或运算   对应数位都是0，结果数位才是0，否则为1
#print(4<<1) #8 向左移动一位，高位溢出舍弃，低位补0  相当于乘以2
#print(4>>1) #2 向右移动一位，高位补0，低位舍弃 相当于除以2

#python中运算符的优先级
#算术运算中 幂运算>乘除运算>加减运算
#位运算中  左右移位运算>按位与运算>按位或运算
#算术运算>位运算>比较运算>布尔运算>赋值运算
