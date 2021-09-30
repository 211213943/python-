#列表的各种操作  python中的列表相当于其他语言中的数组
'''a=10  #变量存储的是一个对象的引用
lst=['hello','world','111']
print(id(lst))       #2695966691904
print(type(lst))     #<class 'list'>
print(lst)           #['hello', 'world', '111']
print(lst[0])        #hello  输出列表的第一个数据   '''
#列表的两种创建方式  1.使用中括号 lst=['111','哈哈']    2.使用内置函数list()  lst=list(['111','哈哈哈'])
#列表的特点  1.列表元素按顺序有序排列   2.索引映射唯一数据  3.列表可以存储重复数据  4.任意类型数据混存 5.根据需要动态分配和回收存储
#列表的查询操作
#1.获取列表中指定元素的索引  index()  如查询列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
#如果查询的元素在列表中不存在，则会抛出ValueError  还可以在指定的start和stop之间进行查找
#2.根据索引获取列表中的单个元素 1.正向索引从0到N-1  如lst[0]  2.逆向索引从-N到-1 如lst[-N]  3.指定索引不存在，抛出indexError
lst=['hello','world','111','hello']
print(lst.index('hello'))
'''
#print(lst.index('h'))       #ValueError: 'h' is not in list
print(lst.index('111',1,3))   #2      '''

'''lst=['hello','world','111','hello']
print(lst[2])   #111  获取索引为2的元素
print(lst[-2])  #111
print(lst[-4])  #hello   '''

#获取列表中的多个元素
#列表名[start:stop:step]  step为整数时，step省略时默认为1,start省略时默认是第一个元素，stop省略时默认是最后一个函数
lst=['hello','world','111','hello']
print(lst[0:1])     #hello
print(id(lst))   #2136380609152
lst2=lst[1:2]    #切片出来的列表是一个新的列表对象
print(id(lst2))  #2136377671936
print(lst[:3])   #['hello', 'world', '111']

#判断指定的元素在列表中是否存在  元素 in 列表名   元素 not in 列表名

#列表元素的遍历   for 迭代变量   in  列表名 :
'''lst=['hello','world','111','hello']
print('g'  in  lst)   #False
print('g' not in  lst) #True
print('hello '  in  lst)   #False

for item in lst:
    print(item)   '''#遍历列表元素

#列表元素的增加操作
'''1.append() 在列表的末尾添加一个元素
2.extend() 在列表的末尾至少添加一个元素
3.insert() 在列表的任意位置添加一个元素
4.切片      在列表的任意位置添加至少一个元素  '''
''' lst=['hello','world','111','hello']
lst.append('hello')
print(lst)    #['hello', 'world', '111', 'hello', 'hello']
lst2=['he',"hh"]
#lst.append(lst2)   #将lst2作为一个元素添加到列表的末尾
#print(lst)   #['hello', 'world', '111', 'hello', 'hello', ['he', 'hh']]
lst.extend(lst2)   #向列表的末尾一次性添加多个元素
print(lst)    #['hello', 'world', '111', 'hello', 'hello', 'he', 'hh']   
lst.insert(1,20)  #向列表的指定位置添加元素,第一个数字指定位置，第二个数字指定元素
print(lst)                
lst3=[10,20,30] 
lst[1:2]=lst3     #将原列表的指定位置切掉，然后用新的列表中的元素替换原列表中的元素
print(lst)        #['hello', 10, 20, 30, '111', 'hello']
print(lst[2])     #20   '''

#列表元素的删除操作
'''1.remove()   一次删除一个元素，重复元素只删除一个，元素不存在抛出ValueError
2.pop()      删除一个指定索引位置上的元素，指定索引不存在抛出IndexError,不指定索引，删除列表中最后一个元素
3.切片        一次至少删除一个元素,但是切片会产生一个新的列表对象,原列表不发生改变
4.clear()    清空列表
5.del        删除列表          '''
lst=[10,20,30,30,140]
'''lst.remove(30)
print(lst)     #[10, 20, 30, 140]
#lst.remove(50)  #ValueError: list.remove(x): x not in list
lst.pop(1)
print(lst)    #[10, 30, 140]
lst.pop()
print(lst)    #[10, 30]   '''
'''
new_lst=lst[1:3]
print(lst)          #[10, 20, 30, 30, 140]
print(new_lst)      #[20, 30]    '''

'''不产生新的列表对象，而是删除原列表中的内容'''
'''lst[1:3]=[]
print(lst)    #[10, 30, 140]   '''

'''lst.clear()
print(lst)    #[]   '''

'''del语句将列表对象删除
del lst
print(lst)    #name 'lst' is not defined    lst列表已经被删除了   '''