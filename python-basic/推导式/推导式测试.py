#TODO 列表推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)
"""
['ALICE', 'JERRY', 'WENDY', 'SMITH']
"""


#计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
"""
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
"""

#TODO 字典推导式
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)

"""
{'Google': 6, 'Runoob': 6, 'Taobao': 6}
"""

#提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)
"""
{2: 4, 4: 16, 6: 36}
"""
#TODO 集合推导式
#计算1,2,3的平方
setnew = {i**2 for i in (1,2,3)}
print(setnew)
"""
{1, 4, 9}
"""

#判断不是 abc 的字母并输出：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

"""
{'r', 'd'}
"""

#TODO 元组推导式
#生成一个包含数字 1~9 的元组
t= (x for x in range(1,10))
print(t)            #<generator object <genexpr> at 0x00000230AACDF148>
print(tuple(t))     #(1, 2, 3, 4, 5, 6, 7, 8, 9)