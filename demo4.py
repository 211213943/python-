#程序的组织结构  1.顺序结构  2.选择结构  3.循环结构
#对象的bool值
#python一切皆是对象，所有对象都有一个bool值，获取对象的bool值，使用内置函数bool()
#以下对象的bool值均是False
#False  数值0  None 空字符串 空列表  空元组 空字典 空集合   剩余其它对象的bool值均为True
'''print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))    '''
#print(bool("helloworld"))  #True

'''age=input("请输入您的年龄")
if age:   #如果输入0，age这个对象的bool值为False，程序继续执行 如果输入非0，age这个对象的bool值为True，程序也会继续执行 
    print(age)
else:
    print('年龄为',age) '''

#选择结构  1.单分支结构 if
'''money=1000
s=int(input("请输入取款金额"))
if s<=money:
    money=money-s
    print("取款成功,余额为",money) '''
#2.双分支结构
'''money=1000
s=int(input("请输入取款金额"))
if s<=money:
    money=money-s
    print("取款成功,余额为",money)
else:
    print("余额不足")  '''
#3.多分支结构
'''score=int(input("请输入你的成绩"))
if score>=90 and score<=100:
    print("A")
elif score>=80 and score<90:
    print("B")
elif score>=70 and score<80:
    print("C")
elif score>=60 and score<70:
    print('D')
elif score>=0 and score<=59:
    print('E')
else:
    print('您好 您的成绩有误')  '''
#4.嵌套if

#条件表达式  条件表达式是if...else的简写
#语法结构   x if  判断条件  else   y   如果判断条件的布尔值为True,条件表达式的返回值为x,否则条件表达式的布尔值为False，返回值为y
'''num_a=int(input("请输入第一个整数"))
num_b=int(input("请输入第二个整数"))
print('使用条件表达式进行比较')
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b)) '''









