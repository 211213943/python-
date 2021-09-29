#流程控制语句break   用于结束循环结构，通常和分支结构if一起使用
'''for item in range(3):
    pwd=input("请输入密码")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")   '''

#流程控制语句continue  用于结束当前循环，进入下次循环，通常与分支结构中的if一起使用
'''要求输出1到50之间所有5的倍数 使用continue'''
'''for  item in range(1,51):
    if item%5!=0:
        continue
    print(item)   '''


#else语句   else语句配合使用的三种情况  1.  if....else  2. while....else 没有碰到break时执行else
#3. for...else     没有碰到break时执行else
'''for  item  in  range(3):
    pwd=input("请输入密码")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
else:
    print("对不起，三次密码均不正确")  '''


#嵌套循环  循环结构中又嵌套了另外的完整的循环结构，其中内层循环时外层循环的循环体执行
''' 打印一个三行四列的矩形
for i in range(3):
    for j in range(4):
        print('*',end='\t')  #不换行输出* \t为一个制表格的距离
    print()  #换行   '''

'''打印九九乘法表
for i in range(1,10):  #行数
    for j  in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()      '''

#二层循环中的break和continue用于控制本层循环
'''for i in  range(5):
    for  j in range(1,11):
        if j%2==0:
            break
        print(j)
#输出结果为五个1   '''

