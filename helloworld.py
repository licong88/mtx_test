# print("Hello world!")
"""
自我介绍
我的名字:
工作地址:
通过python训练营学到什么：
最后打印出来
print()
"""
# print("自我介绍")
# print("我的名字：Iris")
# print("工作地址：广东深圳")
# print("通过python训练营学到什么：了解自动化")
# print("""
# 自我介绍
# 我的名字: Iris
# 工作地址：广东深圳
# 通过python训练营学到什么：：了解自动化
# """)
#
# print(
#     '''
#     へ     ／|
#   /＼7    ∠＿/
#   / │   ／ ／
#  │ Z ＿,＜ ／   /`ヽ
#  │     ヽ   /  〉
#   Y     `  /  /
#  ｲ● ､ ●  ⊂⊃〈  /
#  ()  へ    | ＼〈
#   >ｰ ､_  ィ  │ ／／
#   / へ   / ﾉ＜| ＼＼
#   ヽ_ﾉ  (_／  │／／
#   7       |／
#   ＞―r￣￣`ｰ―＿
#     ''')

# print 默认换行，不换行：加（，end=" "）
# print('hello world', end=' ')
# print('hello world', end=' ')

print('what\'s your name?')

"""
作业题：
我的名字：{}
现居住地：{}
主要使用{}方便测试工作
平时喜欢做{}
座右铭：{}
通过这次训练营想收获：{}
"""

name = 'iris'
addr = 'shenzhen'
tool = 'jmeter'
fun = 'reading'
tuth = 'do yourself'
gett = 'get auto skill'

print(
    """
我的名字：{}
现居住地：{}
主要做{}方便测试工作
平时喜欢做{}
座右铭：{}
通过这次训练营想收获：{}
    """.format(name, addr, tool, fun, tuth, gett)
)