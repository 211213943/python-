'''面向对象的三大特征    1.封装 提高程序的安全性  在python中没有专门的修饰符用于属性的私有，
如果该属性不希望在类对象外部被访问，前面使用两个'_'
2.继承 提高代码的复用性     3.多态  提高程序的可扩展性和可维护性'''
#封装的实现
'''class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在类的外部被使用，所以添加了两个__
    def show(self):
        print(self.name,self.__age)
stu=Student('张三',20)
stu.show()
#在类的外部使用name和age
print(stu.name)
#print(stu.__age)
#print(dir(stu))
print(stu._Student__age)  '''#在类的外部可以通过_Student__age访问类中不想被外部访问的属性

#继承的语法格式   class 子类类名(父类1，父类2...):
#                      pass
#如果一个类中没有继承任何类，则默认继承object，Python支持多继承，定义子类时，必须在其构造函数中调用父类的构造函数
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))
#定义子类
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)  #super()函数是用于调用父类的一个方法
        self.score=score
stu=Student('张三',20,100)
stu.info()

