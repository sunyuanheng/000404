#!/usr/bin/env/python3

'''
学生成绩的管理系统 
'''
student=[]
ID =0
def menu():
    print('''
     ============学生成绩系统=============

     |============主功能菜单==============|
     |                                    |
     |   1、录入学生成绩                  |  
     |   2、查询学生成绩                  |
     |   3、删除学生成绩                  |
     |   4、修改学生成绩                  |
     |   5、显示所有学生成绩              |  
     |   0、退出系统                      |
     |                                    |
     |====================================|
     '''
    )
#录入成绩功能
def addInfo():
    while True:
        sname=input('请输入学生姓名')
        if not sname:
            print('姓名不能为空')
            continue
        class1=input('请输入学生的班级')
        linux=input('请输入学生linux成绩')
        PHP=input('请输入学生php成绩')
        python=input('请输入学生python成绩')
        global ID
        ID +=1
        stu={'id':ID,'sname':sname,'class1':class1,'linux':linux,'php':PHP,'python':python}
        student.append(stu)
        print(student)
        key = input('是否继续录入y/n?')
        if key == 'y':
            continue
        else:
            break
#展示学生信息
def show():
    '''
    展示列表，要遍历列表，获取列表中的每一个值
    '''
    format_title='{:^6}{:^12}\t{:^12}{:^12}{:^12}{:^12}'
    format_date='{:^6}{:^13}\t{:^15}{:^14}{:^14}{:^14}'
    print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
    for i in student:
       ID=i.get('id')
       name=i.get('sname')
       class1=i.get('class1')
       linux=i.get('linux')
       php=i.get('php')
       python=i.get('python')
       print(format_date.format(ID,name,class1,linux,php,python))

#查询功能输入姓名查询
def select():
    name=input('请输入要查询学生的姓名')
    for i in student:
        sname=i.get('sname')
        if name==sname:
            format_title='{:^6}{:^12}\t{:^12}{:^12}{:^12}{:^12}'
            format_date='{:^6}{:^13}\t{:^15}{:^14}{:^14}{:^14}'
            print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
            for i in student:
                ID=i.get('id')
                name=i.get('sname')
                class1=i.get('class1')
                linux=i.get('linux')
                php=i.get('php')
                python=i.get('python')
                print(format_date.format(ID,name,class1,linux,php,python))
        else:
            print('姓名输入有误，请重新输入')
            select()
#搜索功能
def search():
    format_title='{:^6}{:^12}\t{:^12}{:^12}{:^12}{:^12}'
    format_date='{:^6}{:^13}\t{:^15}{:^14}{:^14}{:^14}'
    sname=input('请输入要查询的学生姓名')
    print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
    
    name_list=[student[i].get('sname') for i in range(len(student))]
    if sname in name_list:
        for i in student:
            if  sname == i.get('sname'):
                ID=i.get('id')
                name=i.get('sname')
                class1=i.get('class1')
                linux=i.get('linux')
                php=i.get('php')
                python=i.get('python')

                print(format_date.format(ID,name,class1,linux,php,python))
    else:
        print('学生信息不存在')
        search()
#删除学生信息，通过姓名
def delete():
    global ID
    name=input('请输入要删除学生的姓名')
    if student:

        for i in student:
            if name == i['sname']:
                student.remove(i)
                print('删除成功')
     #修改id号减一       
        for i in range(len(student)):
            ID = i+1
            student[i]['ID']= ID
    if not student:
        ID = 0
    #show()
def change():

    change1=input('请输入要修改信息的学生姓名')
    for i in student:
        sname=i.get('sname')
        if change1 ==sname:
            new_name=input('请输入新的姓名')
            i['name']=new_name
            new_class1=input('请输入新的班级')
            i['class1']=new_class1
            new_linux=input('请输入新的linux成绩')
            i['linux']=new_linux
            new_php=input('请输入新的php的成绩')
            i['php']=new_php
            new_python=input('请输入新的python成绩')
            i['python']=new_python
            format_title='{:^6}{:^12}\t{:^12}{:^12}{:^12}{:^12}'
            format_date='{:^6}{:^13}\t{:^15}{:^14}{:^14}{:^14}'

            print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
            print(format_date.format(ID,name,class1,linux,php,python))
        else:
            print('要修改的学生不存在')
#主函数
def main():
     while True:
        menu()
        key = input('请选择功能对应的数字')
        if key =='1':
             addInfo()
        if key=='5':
            show()
        if key =='2':
            search()
        if key == '3':
            delete()
        if key == '4':
            change()
        if key =='0':
            break
main()

