dict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
# print(dict["age"])  #报错
# print(dict.get("age"))  #返回None

if dict.get("name"):
    print(dict.get("name"))   #返回：runoob
if dict.get("age"):
    print(dict.get("age"))    #没有返回

#这两种都可以使用
# name = dict.get("name") if dict.get("name") != None else None
name = dict.get("name") if dict.get("name")  else None
print(name)
print(type(name))

