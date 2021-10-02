#列表元素的修改操作 1.为指定索引的元素赋予一个新值  2.为指定的切片赋予一个新值
'''lst=[10,20,30,40]
lst[1]=100
print(lst)        #[10, 100, 30, 40]
lst[1:3]=[100,200,200,3]
print(lst)           #[10, 100, 200, 200, 3, 40]   '''
'''列表元素的两种排序操作  1.调用sort()方法，列表中的所有元素默认按照从小到大的顺序进行排序，可以指定reverse=True
进行降序排序，是对原列表进行的排序操作 2.调用内置函数sorted(),可以指定reverse=True,进行降序排序，原列表不发生改变，会产生一个新的列表对象'''
'''lst=[10,2,55,22,50]
lst.sort()
print(lst)    #[2, 10, 22, 50, 55]  '''
'''通过指定关键字参数，将列表中的元素进行降序和升序排序
lst.sort(reverse=True)
print(lst)      #[55, 50, 22, 10, 2]
lst.sort(reverse=False)
print(lst)      #[2, 10, 22, 50, 55]   '''

# 原列表没有变化，而是产生了一个新的列表
lst=[2,3,48,55,5]
new_lst=sorted(lst)
print(lst)          #[2, 3, 48, 55, 5]
print(new_lst)      #[2, 3, 5, 48, 55]   '''
'''指定参数实现列表的降序排序
desc_lst=sorted(lst,reverse=True)
print(desc_lst)     #[55, 48, 5, 3, 2]   '''

'''列表生成式(生成列表的公式)  语法格式：   [i*i 表示列表元素的表达式  for i 自定义变量  in range(1,10) 可迭代对象] '''
lst=[i for i  in range(1,10)]
lst1=[i*i for i  in range(1,10)]
print(lst)    #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst1)   #[1, 4, 9, 16, 25, 36, 49, 64, 81]
'''让列表中的元素的值为2,4,6,8,10'''
lst2=[i*2 for i  in range(1,6)]
print(lst2)    #[2, 4, 6, 8, 10]

