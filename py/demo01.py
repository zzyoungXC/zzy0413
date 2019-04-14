
#print('hello')
class Person(object):
    def __init__(self,name):
        #print('1',self)
        self.name=name
        #self.age=age

    def show(self):
        #print('4',self)
        #print(f'姓名：{self.name},年龄:{self.age}')
        print('姓名：%s'%(self.name))

    #def __del__(self):
      #  print('2',self)
class whiteper(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def show(self):
        print(f'姓名：{self.name},年龄:{self.age}')

zzy=whiteper('zzy',20)
print(type(zzy))
zzy.show()
#print('3',zzy)
#del zzy
#input('------')
#zzy.show()
lz=whiteper('lz')
print(type(lz))
lz.show()