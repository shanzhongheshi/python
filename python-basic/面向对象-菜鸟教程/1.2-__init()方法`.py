class Complex:
    def __init__(self,relpart,imagpart):
        self.r=relpart
        self.i=imagpart
"""
x=Complex()
print(x)
报错：TypeError: __init__() missing 2 required positional arguments: 'relpart' and 'imagpart'
结论：定义了有参的__init__()，就必须传参
"""

y=Complex(2,3)
print(y.r,y.i)
