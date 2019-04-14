class Student(object):
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'姓名：{self.name}')
def pr():
    print('1')
#print(__name__)
if __name__=='__main__':
    pr()
    stu=Student('张三')
    stu.show()