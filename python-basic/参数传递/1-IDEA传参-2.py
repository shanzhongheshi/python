# 导入包
import argparse

# 创建解析器
ap = argparse.ArgumentParser()
# 添加位置参数(positional arguments)
ap.add_argument("-n", "--name", required=True,help="someone's name")
ap.add_argument("-a", "--age", required=True,help="someone's age")
args = vars(ap.parse_args())
print(args)                     #{'name': 'zhangsan', 'age': '15'}
print(args["name"],args["age"]) #zhangsan 15
