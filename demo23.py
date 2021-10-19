'''特殊方法  _len_()   通过重写_len_()方法，让内置函数len()的参数可以是自定义类型
              _add_()  通过重写_add_()方法，可使用自定义对象具有"+"功能
              _new_()   用于创建对象
              _init_()  对创建的对象进行初始化   '''
'''a=10
b=20
c=a+b
d=a.__add__(b)
print(c,d)
'''

'''class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2  #实现了两个对象的加法运算（因为在Student类中，编写了__add__()特殊的方法）
print(s)
print(stu1.__add__(stu2))

lst=[11,22,33,44]
print(len(lst))  #4  len()是内置函数，可以计算列表的长度
print(lst.__len__())   #4 
print(len(stu1))     '''  #2





class Person():
    def __new__(cls, *args, **kwargs):
        #这个方法经常用来做单例模式的时候使用
        print("__new__被调用执行了,cls的id值为{0}".format(id(cls)))
        obj=super().__new__(cls)   #cls表示当前这个类   在这里是真正创建对象实例的
        print('创建的对象的id为:{}'.format(id(obj)))
        return obj       #必须有return来返回当前对象
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为:{0}'.format(id(self)))  #self表示当前函数
        self.name=name
        self.age=age
# print('object这个类对象的id为:{0}'.format(id(object)))
# print('Person这个类对象的id为:{0}'.format(id(Person)))

#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id为:{0}'.format(id(p1)))

'''__new__和__init__函数的区别
__new__类的实例方法，必须要返回该实例，否则对象就创建不成功
__init__ 用来做数据属性的初始化工作，也可以认为是实例的构造方法，接受类的实例 self并对其进行构造
__new__  至少有一个参数是cls代表要实例化的类，此参数在实例化时有python解释器自动提供
__new__的执行是早于__init__方法的'''