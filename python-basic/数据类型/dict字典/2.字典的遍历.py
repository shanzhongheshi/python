d = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
#TODO 使用items(),返回一个视图对象
for k,v in d.items():
    print(k,v)

"""
name runoob
code 1
site www.runoob.com
"""

#TODO 遍历所有的key
for k in d:
    print(k)

"""
name
code
site
"""
#TODO 遍历所有的value,返回一个视图对象
for v in d.values():
    print(v)
"""
runoob
1
www.runoob.com
"""