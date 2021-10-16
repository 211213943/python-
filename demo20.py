#python是动态语言，在创建对象之后，可以动态地绑定属性和方法
class Student:
    def __init__(self,name,age):       #初始化方法
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',30)
stu2.gender='男'   #动态绑定属性


'''动态绑定方法'''
def show():
    print('我是一个定义在类之外的函数')
stu1.show=show
stu1.show()