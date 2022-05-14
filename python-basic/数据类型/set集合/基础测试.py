#TODO 1.创建空集合，不能用{}，而是用set()
m={}
print("m的数据类型："+str(type(m)))
n=set()
print("n的数据类型："+str(type(n)))
"""
m的数据类型：<class 'dict'>
n的数据类型：<class 'set'>
"""

#TODO 2.重复元素可以存在吗
# 不可以
l={1,2,2,3}
print("l的数据类型："+str(type(l)))
print(l)
"""
l的数据类型：<class 'set'>
{1, 2, 3}
"""

#TODO 3.集合可以包含不同类型的元素吗
# 可以
o={1,"dkjf",4}
print("o的数据类型："+str(type(o)))
print(o)
"""
o的数据类型：<class 'set'>
{1, 'dkjf', 4}
"""

#TODO 4.集合如何添加元素
a=set()
a.add(1)
a.add("kdj")
print("a的数据类型："+str(type(a)))
print(a)
"""
a的数据类型：<class 'set'>
{1, 'kdj'}
"""