from time import sleep
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
print (counter.publicCount)
sleep(3)
print (counter.__secretCount)  # 报错，实例不能访问私有变量

"""
1
1
Traceback (most recent call last):
  File "D:/code2022/python/python-basic/面向对象-菜鸟教程/3.类的私有属性.py", line 15, in <module>
    print (counter.__secretCount)  # 报错，实例不能访问私有变量
AttributeError: 'JustCounter' object has no attribute '__secretCount'
"""