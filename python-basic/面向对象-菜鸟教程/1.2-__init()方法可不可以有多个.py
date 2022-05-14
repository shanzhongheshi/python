class Complex:
    r=0
    i="2"
    def __int__(self):
        return self
    def __init__(self,relpart,imagpart):
        self.r=relpart
        self.i=imagpart
"""
x=Complex()
print(x)
报错：TypeError: __init__() missing 2 required positional arguments: 'relpart' and 'imagpart'
结论：不行，只能有一个
"""

