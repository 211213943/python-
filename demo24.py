'''变量的赋值操作   只是形成两个变量，实际上还是指向同一个对象
浅拷贝：python一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象和拷贝对象会引用同一个对象
深拷贝：使用copy模块和deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同'''
class  Cpu():
    pass
class  Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#(1)变量的赋值
cpu1=Cpu()
cpu2=cpu1
print(cpu1)      #<__main__.Cpu object at 0x000001EC2F592FD0>
print(cpu2)      #<__main__.Cpu object at 0x000001EC2F592FD0>
#(2)类的浅拷贝
disk=Disk()
computer=Computer(cpu1,disk)

#浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

#深拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)