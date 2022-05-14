class Test:
    def prt(self):
        print(self)
        print(self.__class__)

x=Test()
x.prt()

"""
<__main__.Test object at 0x000002026185E0C8>
<class '__main__.Test'>
"""