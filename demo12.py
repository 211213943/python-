'''集合是python语言提供的内置数据结构，集合中的元素不允许重复，集合中的元素是无序的，集合与列表，字典一样都属于可变类型的序列，集合是没有value的字典
集合的创建方式 1.直接{} s={'python',22,33}   2.使用内置函数set()
s=set(range(5))
print(s)          #{0, 1, 2, 3, 4}
print(set([3,4,5]))             #{3, 4, 5}
print(set((22,33,44)))          #{33, 44, 22}
print(set({222,333,444}))       #{444, 333, 222}
print(set())                   #set()
print(set('python'))         #{'n', 'y', 'p', 'h', 'o', 't'}        '''

'''定义空集合,只能使用set()定义空集合，如果使用s1={}，则默认建立的是空字典
s1=set()      '''

'''集合的相关操作  1.集合元素的判断操作 in 或not in   2.集合元素的新增操作 调用add()方法，一次添加一个元素
调用update()方法至少添加一个元素  3.集合元素的删除操作  3.1调用remove()方法，一次删除一个指定元素，如果指定的
元素不存在抛出KeyError  3.2调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛出异常
3.3 调用pop()方法，一次只删除一个任意元素  3.4 调用clear()方法。清空集合'''

'''s={10,20,30,40}
print(10 in s)   #True
s.add(22)
print(s)        #{40, 10, 20, 22, 30}
s.update({200,400,300})   #向集合中添加集合
print(s)          #{40, 200, 10, 300, 400, 20, 22, 30}
s.update([10,11]) #向集合中添加列表
s.update((55,7))   #向集合中添加元组   '''

'''s={10,20,30,40}
s.remove(10)
#s.remove(22)     #KeyError: 22
s.discard(22)
s.pop()    #删除任意一个元素，pop方法中不能添加参数
print(s)
s.clear()
print(s)        '''

'''集合之间的关系  1.两个集合是否相等  可以使用运算符==或者!=进行判断
2.一个集合是否是另一个集合的子集，可以调用issubset方法进行判断
3.一个集合是否是另一个集合的超集，可以调用issuperset方法进行判断
4.两个集合是否没有交集，可以调用方法isdisjoint进行判断
s={10,20,30,40}
t={10,20,40}
print(s==t)      #False
print(s!=t)      #True
print(t.issubset(s))  #True  t是s的子集
print(s.issuperset(t))  #True  s是t的超集
print(s.isdisjoint(t))  #False  s和t有交集  '''

'''集合的数学操作
#交集
s1={10,20,30,40}
s2={10,20,30}
print(s1.intersection(s2))     #{10, 20, 30}
print(s1 & s2)                 #{10, 20, 30}  与运算
#并集
print(s1.union(s2))            #{20, 40, 10, 30}
print(s1 | s2)                 #{20, 40, 10, 30}
#差集操作
print(s1.difference(s2))      #40
print(s1-s2)                  #40
#对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)           '''

#集合生成式  {i*i for i in range(1,10)}
s={i for i in range(10)}
print(s)
