str="""{'name': ['runoob','zhangsan'],'code':1, 'site': 'www.runoob.com'}"""
print(type(str))
print(type(eval(str)))
"""
<class 'str'>
<class 'dict'>
"""
dict=eval(str)
print(dict["name"])
print(type(dict["name"]))
"""
['runoob', 'zhangsan']
<class 'list'>
"""