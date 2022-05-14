#属性引用和实例化

class MyClass:
    i=123
    def f(self):
        return "hello python"

x=MyClass()

print("MyClass类的属性i为",x.i)
print("MyClass类的方法f输出为"+x.f())
"""
MyClass类的属性i为 123
MyClass类的方法f输出为hello python
"""