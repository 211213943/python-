#方法重写，如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
#子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
'''class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)  #super()函数是用于调用父类的一个方法
        self.score=score
    def info(self):
        super().info()
        print('分数:{0}'.format(self.score))
stu=Student('李四',20,100)
stu.info()   '''

#object类是所有类的父类。内置函数dir()可以查看指定对象的所有属性
#print(dir(object))

'''多态：简单的说，多态就是“具有多种形态”，它指的是：即使不知道一个变量所引用的对象到底是什么类型，仍然可以
通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法    '''
'''class  Animal():
    def eat(self):
        print("动物要吃东西")
class Dog(Animal):
    def eat(self):
        print("狗吃肉")
class Cat(Animal):
    def eat(self):
        print("猫吃鱼")
class Person(object):
    def eat(self):
        print("人吃五谷杂粮")
        
def fun(animal):
    animal.eat()
fun(Dog())
fun(Cat())
fun(Person())   '''

#特殊方法和特殊属性
'''1.特殊属性  _dict_  获得类对象或实例对象所绑定的所有属性和方法的字典
   2.特殊方法  _len_()   通过重写_len_()方法，让内置函数len()的参数可以是自定义类型
              _add_()  通过重写_add_()方法，可使用自定义对象具有"+"功能
              _new()_   用于创建对象
              _init_()  对创建的对象进行初始化          '''
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name):
        self.name=name
#创建C类的对象
x=C('张三')
print(x.__dict__)   #查看实例对象的属性字典
#print(C.__dict__)
print(x.__class__)   #<class '__main__.C'>   输出该对象所属的类
print(C.__class__)
print(C.__bases__)   #(<class '__main__.A'>, <class '__main__.B'>)   输出结果为一个元组，输出父类类型
print(C.__base__)   #<class '__main__.A'>
print(C.__mro__)  #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)  类的层次结构
print(A.__subclasses__())  #子类的列表






