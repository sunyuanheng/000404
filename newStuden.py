#!/usr/bin/env python3
"""
**      * 学生成绩管理系统
**      * 录入功能
**      * 查询功能
**      * 删除功能
**      * 修改功能
**      * 显示所有
**      * 数据字段：学生姓名，学生班级，学生所学课程
**      * id自增长
**      * stu1 = {'id':1,'sname':'tom','class':1,'linux':100}
"""

Id = 0
stu_info = []

def menu():
    print("""
    |----------学生管理系统---------|
    
    |===========主功能菜单==========|
    |                               |
    |    1，录入学生成绩            |
    |    2，查询学生成绩            |
    |    3，删除学生成绩            |
    |    4，修改学生成绩            |
    |    5，显示所有成绩            |
    |    6，退出系统                |
    |                               |
    |===============================|
    """)

"""
**
**      * 函数名：addIonfo
**      * 功能：添加学生信息
**
"""
def addInfo():
    while True:
        sname = input('输入学生姓名：')
        if not sname:
            print('名字不能为空，请重新输入')
            addInfo()
        else:
            bj = input('输入学生班级：')
            linux = input('输入学生linux成绩：')
            php = input('输入学生php成绩：')
            python = input('输入学生python成绩：')
            global Id
            Id += 1
            stu = {'Id':Id,'sname':sname,'bj':bj,'linux':linux,'php':php,'python':python}
            stu_info.append(stu)
            num = input('Y/y，继续  N/n，退出：')
            thisFunction = addInfo
            ifTrue(num,thisFunction)

"""
**
**      * 函数名：search
**      * 功能：查询单个指定名字的学生成绩信息
**
"""
def search():
    format_title = '{:^6}{:^12}\t{:^10}{:^10}{:^10}{:^10}'
    format_data  = '{:^6}{:^14}\t{:^10}{:^10}{:^10}{:^10}'
    sname = input('输入查询的学生姓名：')
    print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
    name_list = [stu_info[i].get('sname') for i in range(len(stu_info))]
    if sname in name_list:
        for i in stu_info:
            if sname == i.get('sname'):
                Id = i.get('Id')
                sname = i.get('sname')
                bj = i.get('bj')
                linux = i.get('linux')
                php = i.get('php')
                python = i.get('python')
                print(format_data.format(Id,sname,bj,linux,php,python))
    else:
        print("学生信息不存在")
    num = input('Y/y，继续  N/n，退出：')
    thisFunction = search
    ifTrue(num,thisFunction)

"""
**
**      * 函数名：delete
**      * 功能：删除指定单个学生
**
"""
def delete():
    sname = input('请输入学生姓名：')
    for i in stu_info:
        if i['sname'] == sname:
            Id = i.get('Id')
            stu_info.remove(i)
            print('删除成功')
            for a in stu_info:
                if a['Id'] > Id:
                    Ids = a.get('Id') - 1
                    a['Id'] = Ids
    num = input('Y/y，继续  N/n，退出：')
    thisFunction = delete
    ifTrue(num, thisFunction)

"""
**
**      * 函数名：modify
**      * 功能：修改指定学生的成绩，不允许修改id，姓名，班级
**
"""
def modify():
    sname = input('请输入学生名字：')
    global stu_info
    for i in stu_info:
        if i['sname'] == sname:
            Id = i.get('Id')
            stuId = Id - 1
            sname = i.get('sname')
            bj = i.get('bj')
            newLinux = input('请输入学生linux成绩：')
            newPHP = input('请输入学生php成绩：')
            newPython = input('请输入学生python成绩：')
            newStudent = {"id":Id,"sname":sname,"bj":bj,'linux':newLinux,'php':newPHP,'python':newPython}
            stu_info[stuId].update(newStudent)
            num = input('Y/y，继续  N/n，退出：')
            thisFunction = modify
            ifTrue(num, thisFunction)

"""
**
**      * 函数名：show
**      * 功能：查询全部学生成绩信息
**
"""
def show():
    format_title = '{:^6}{:^12}\t{:^10}{:^10}{:^10}{:^10}'
    format_data  = '{:^6}{:^14}\t{:^10}{:^10}{:^10}{:^10}'
    print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
    for i in stu_info:
        Id = i.get('Id')
        sname = i.get('sname')
        bj = i.get('bj')
        linux = i.get('linux')
        php = i.get('php')
        python = i.get('python')
        print(format_data.format(Id,sname,bj,linux,php,python))

"""
**
**      * 函数名：ifTrue
**      * 功能：判断用户是否继续在当前被调用函数里操作
**      * 该函数可以被任何功能函数调用，调用是，传入参数
**      * num参数，获取用户输入的选项
**      * thisFunction参数，获取调用ifTrue函数的函数
**
"""
def ifTrue(num,thisFunction):
    if num == "Y" or num == "y":
        thisFunction()
    elif num == "N" or num == "n":
        main()
    else:
        num = input('请输入正确选项  Y/y,继续  N/n,退出:')
        ifTrue(num,thisFunction)

"""
**
**      * 函数名：main
**      * 功能：主函数，判断用户输入的数字，并调用相关功能
**
"""
def main():
    while True:
        menu()
        numExit = input('请选择菜单选项：')
        if numExit == "1":
            addInfo()
        elif numExit == "2":
            search()
        elif numExit == "3":
            delete()
        elif numExit == "4":
            modify()
        elif numExit == "5":
            show()
        elif numExit == "6":
            exit()
        else:
            print('请输入正确选项')

main()