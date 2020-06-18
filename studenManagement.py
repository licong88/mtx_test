# @File: studentManage.py
# @Author: 夭夭
# @Time: 五月 21, 2020

# 需求：进入系统显示系统功能界面，功能如下：
#
# 1-- 添加学员--存储结构[{'name':,'id':,'tel':}，{}，{}] 每一个字典都是学员的信息
# 2-- 删除学员
# 3-- 修改学员信息
# 4-- 查询学员信息
# 5-- 显示所有学员信息
# 6-- 退出系统

# 系统共6个功能，用户根据自己需求选取
#
info_list = []
# 打印菜单
def info_print():

    print('''
    ----------------
    欢迎登录学员管理系统
    1-- 添加学员
    2-- 删除学员
    3-- 修改学员信息
    4-- 查询学员信息
    5-- 显示所有学员信息
    6-- 退出系统
    ----------------
    ''')
# 用户输入序号选择功能
# 1.添加学员
def add_info():
    # 接收用户输入的学生信息学号，姓名和手机号
    stu_num = input('请输入新增学员学号：')
    stu_name = input('请输入新增学员姓名:')
    stu_tel = input('请输入新增学员手机号:')
    if stu_name and stu_num and stu_tel:
        # 声明修改全局变量
        global info_list
        for i in info_list:
            if i['id'] == stu_num:
                print('您输入的用户姓名已经存在，请重新输入')
                break
        else:
            # 如果循环正常结束，就会执行else后面的代码，否则就不会执行不正常结束break
            # 用户不存在，把学生信息放入字典，然后追加到列表
            info_dict = {}
            info_dict['name']= stu_name
            info_dict['id'] = stu_num
            info_dict['tel'] = stu_tel
            info_list.append(info_dict)

            # info_list.append({'name':stu_name,'id':stu_num,'tel':stu_tel})

            print(info_list)
    else:
        print('您输入的姓名，学号和手机号码都不能为空')

# 2，删除学员
def del_info():
    stu_num = input('请输入你删除学员的学号：')
    # 首先要判断学员的姓名是否在列表里面
    global info_list
    for i in info_list:
        if i['id'] ==stu_num:
            info_list.remove(i)
            print('恭喜删除成功')
            break
    else:
        print('用户不存在')

#3.修改学员信息----修改手机号码
def modify_info():
    stu_num = input('请您输入要修改信息的学员学号：')
    global info_list
    for i in info_list:
        if i["id"] == stu_num:
            i['tel'] = input('请输入您要更改之后的手机号码：')
            print(info_list)
            print('修改成功')

#4.查询学员信息
def search_info():
    stu_num = input('请输入你要查询的学员学号:')
    for i in info_list:
        if i['id']==stu_num:
            stu_name = i['name']
            stu_tel = i['tel']
            print(f'此学生的学号是{stu_num},姓名是{stu_name},电话号码是{stu_tel}')
            break
    else:
        print('用户不存在')

#5.显示所有学员信息
def show_info():
    for i in info_list:  #i--->学员信息，字典
        stu_name = i['name']
        stu_num = i['id']
        stu_tel = i['tel']
        print(f'{stu_name}的学号是{stu_num},电话是{stu_tel}')
    print('所有学员信息展示完毕')



#6.入口 业务组合 运行的入口--写业务流程
def main():
    while True:
        # 打印操作菜单
        info_print()
        # 用户进行选择
        user_num = input('请选择您需要输入的功能序号：')

        if user_num == "1":
            #添加学员
            # print('添加学员')
            add_info()
        elif user_num == "2":
            #删除学员
            # print('删除学员')
            del_info()
        elif user_num == "3":
            #修改学员信息
            modify_info()
        elif user_num == "4":
            #查询学员信息
            search_info()
        elif user_num == "5":
            #显示所有学员信息
            show_info()
        elif user_num == '6':
            break
        else:
            print('输入错误，请重新输入！！！')


if __name__ == '__main__':
    main()




