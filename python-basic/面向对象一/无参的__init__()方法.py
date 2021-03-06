"""定义了一个英雄类，可以移动和攻击"""
# Python 的类里提供的，两个下划线开始，两个下划线结束的方法，就是魔法方法，__init__()就是一个魔法方法，通常用来做属性初始化 或 赋值 操作。
# 如果类面没有写__init__方法，Python会自动创建，但是不执行任何操作，
# 如果为了能够在完成自己想要的功能，可以自己定义__init__方法，
# 所以一个类里无论自己是否编写__init__方法 一定有__init__方法。
class Hero(object):
    def __init__(self):
        """ 方法，用来做变量初始化 或 赋值 操作，在类实例化对象的时候，会被自动调用"""
        self.name = "泰达米尔" # 姓名
        self.hp = 2600 # 生命值
        self.atk = 450  # 攻击力
        self.armor = 200  # 护甲值

    def move(self):
        """实例方法"""
        print("正在前往事发地点...")

    def attack(self):
        """实例方法"""
        print("发出了一招强力的普通攻击...")


# 实例化了一个英雄对象，并自动调用__init__()方法
taidamier = Hero()

# 通过.成员选择运算符，获取对象的实例方法
taidamier.move()
taidamier.attack()