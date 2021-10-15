class Student:   #Student为类的名称，类名由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_place='河南'  #直接写在类里的变量，称为类属性，被该类的所有对象所共享

    #初始化方法
    def __init__(self,name,age):
        self.name=name   #self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给了实体变量
        self.age=age

    #类中的实例方法，在类之外的定义的称为函数，在类之内定义的称为方法
    def eat(self):
        print('学生在吃饭')

    #静态方法   使用@staticmethod修饰的方法，使用类名直接访问的方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以是静态方法')

    #类方法   使用@classmethod修饰的方法，使用类名直接访问的方法
    @classmethod
    def cm(cls):
        print('我使用了classmethod进行修饰，所以我是类方法')

#python中一切皆对象,Student类也是一个类对象
'''print(id(Student))           #2570955314448
print(type(Student))         #<class 'type'>
print(Student)            '''   #<class '__main__.Student'>

#对象的创建又称为类的实例化  语法:实例名=类名()   有了实例，就可以调用类中的内容

#创建Student类的实例对象
stu1=Student('张三',20)
'''stu1.eat()            #学生在吃饭
Student.eat(stu1)     '''#学生在吃饭     33行与32行的代码功能相同，都是调用Student中的eat方法
print(Student.native_place)   #访问类属性
Student.method()
Student.cm()

