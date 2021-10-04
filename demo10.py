'''字典是python内置的数据结构之一，与列表一样是一个可变序列，字典以键值对的方式存储数据，字典是一个无序的序列
scores={'张三':100,'李四':99}'''

'''字典的创建   1.使用花括号  scores={'张三':100,'李四':99}  2.使用内置函数dict()
dict(name='jack',age=20) '''
'''student=dict(name='jack',age=20)
print(student)    #{'name': 'jack', 'age': 20}
print(type(student))     #<class 'dict'>   '''
'''创建空字典
dict={}
print(dict)    '''

'''字典中元素的获取  1.[]  例如scores['张三']  2.使用get()方法  scores.get('张三')
二者之间的差别   []如果字典中不存在指定的key，则会抛出keyError异常。get()方法取值，如果字典中不存在指定的key，
并不会抛出keyError而是返回None，可以通过参数设置默认的value，以便指定的key不存在时返回  
scores={'张三':100,'李四':99}
print(scores['张三'])   #100
#print(scores['王五'])       #KeyError: '王五'

print(scores.get('张三'))  #100
print(scores.get('王五'))    #None
print(scores.get('陈六',55))   #55是在查找'陈六'所对应的value不存在时，提供的一个默认值   '''


'''字典中key的判断  in 和 not in  指定的key在字典中存在/不存在时返回True
字典元素的删除  del score['张三']
字典元素的新增  score['Jack']=90    
scores={'张三':100,'李四':99}
print('张三' in scores)   #True
del scores['张三']   #删除指定的键值对
print(scores)   #{'李四': 99}
#scores.clear()  #清空字典中的元素
#print(scores)
scores['陈六']=88  #新增字典中的元素
print(scores)   #{'李四': 99, '陈六': 88}
scores['陈六']=44    #修改字典中元素的值
print(scores)    #{'李四': 99, '陈六': 44}   '''

'''获取字典视图的三个方法   1.keys()  获取字典中所有key  2.values()获取字典中所有的value 3.items()获取字典中所有的key，value对
scores={'张三':100,'李四':99}
keys=scores.keys()
print(keys)     #dict_keys(['张三', '李四'])
print(type(keys))    #<class 'dict_keys'>
print(list(keys))    #['张三', '李四']  将所有的key组成的视图转换成列表
values=scores.values()
print(values)   #dict_values([100, 99])
items=scores.items()
print(items)     ''' #dict_items([('张三', 100), ('李四', 99)])

'''字典元素的遍历   for item in scores:
                     print(item)      
scores={'张三':100,'李四':99}
for  item  in  scores:
    print(item)   #输出字典中所有的键
    print(item,scores[item])     '''   #输出字典中的键和值

'''字典的特点 1.字典中的所有元素都是一个key——value对，key不允许重复，value可以重复  2.字典中的元素是无序的
3.字典中的key必须是不可变对象  4.字典也可以根据需要动态地伸缩  5.字典会浪费较大的内存，是一种使用空间换时间的数据结构
d={'name':'张三','name':'李四'}
print(d)    #{'name': '李四'}   key值重复时会出现值覆盖的情况    '''

#字典生成式   内置函数zip()，用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组
#组成的列表   {item.upper():price for item,price in zip(items,prices)}
'''items=['fruits','books','others']
prices=[96,78,85]
d={ item:price  for item,price in zip(items,prices)}
c={ item.upper():price  for item,price in zip(items,prices)}   
print(d)    #{'fruits': 96, 'books': 78, 'others': 85}
print(c)    #{'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 85}  '''
{'plane': 0, 'car': 0, 'bird': 0, 'cat': 0, 'deer': 0, 'dog': 0, 'frog': 0, 'horse': 0, 'ship': 0, 'truck': 0}



