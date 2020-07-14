#!/usr/bin/env python3

'''
    字段：学生姓名 班级 Linux PHP Python
    stu1 = {'id':1,'sname':'tom','bj':'1','Linux':100,}
'''

stu_info = []
id = 0

def menu():
    print('''
      | ----------学生成绩系统--------|
      |                               |
      | ==========主功能菜单==========|
      |                               |
      |                               |                               
      |      1.录入学生成绩           |
      |      2.查询学生成绩           |
      |      3.删除学生的成绩         |
      |      4.修改学生的成绩         |
      |      5.展示所有学生成绩       |
      |      0.退出系统               |
      |                               |
      |-------------------------------|





    ''')

#录入学生成绩
def add_info():
    while True:
        sname = input('输入学生的姓名:')
        if not sname:
            print('学生姓名不能为空')
            continue
        bj = input('输入学生的班级:')
        Linux = input('输入Linux成绩:')
        PHP = input('输入PHP成绩:')
        Python = input('输入Python成绩:')

        global id 
        id += 1
        stu = {'id':id,'sname':sname,'bj':bj,'Linux':Linux,'PHP':PHP,'Python':Python}
        stu_info.append(stu)

        print(stu_info)
        key = input('是否继续录入y/n?')
        if key == 'y':
            continue
        else:
            break


#显示所有学生的成绩
def show():
    '''
    遍历列表，获取到每个学生的信息
    '''
    format_title = '{:^6}{:^12}\t{:^12}{:^12}{:^12}{:^12}'
    format_data = '{:^6}{:^13}\t{:^15}{:^13}{:^15}{:^14}'
    print(format_title.format('ID','姓名','班级','Linux成绩','PHP成绩','Python成绩'))

    for i in stu_info:
        id = i.get('id')
        sname = i.get('sname')
        bj = i.get('bj')
        Linux = i.get('Linux')
        PHP = i.get('PHP')
        Python = i.get('Python')
        print(format_data.format(id,sname,bj,Linux,PHP,Python))

def search():
    '''
    根据名字查询学生的成绩

    '''
    
    format_title = '{:^6}{:^12}\t{:^12}{:^12}{:^12}{:^12}'
    format_data = '{:^6}{:^13}\t{:^15}{:^13}{:^15}{:^14}'
    sname  = input('输入要查询学生的姓名:')

    print(format_title.format('ID','姓名','班级','Linux成绩','PHP成绩','Python成绩'))
    
    #提取到所有学生的名字
    name_list = [stu_info[i].get('sname') for i in range(len(stu_info))]
    if sname in name_list:
        for i in stu_info:
            if sname == i.get('sname'):
                id = i.get('id')
                sname = i.get('sanme')
                bj = i.get('bj')
                Linux = i.get('Linux')
                PHP = i.get('PHP')
                Python = i.get('Python')
                print(id,sname,bj,Linux,PHP,Python)
    else:
        print('学生名字不存在')


def delete():
    global id
    sname = input('请输入要删除学生得名字：')

    if stu_info:
        for i in stu_info:
            if i['sname'] == sname:
                stu_info.remove(i) #删除该字段
                print('删除成功')
    #修改剩下学生的id id - 1
    #for i,v in enumerate(stu_info):
    for i in range(len(stu_info)):
        id = i + 1
        stu_info[i]['id'] = id
    if not stu_info:
        id = 0
    show()

#修改学生信息，只修改学生的成绩
def modify():
    sname = input('请输入学生名字：')
    global stu_info    
    for i in stu_info:
        if i['sname'] == sname:
            id = i.get('id')
            stuid = id - 1
            sname = i.get('sname')
            bj = i.get('bj')
            stuNum = i.get('stuNum')
            newLinux = input('请输入学生linux成绩：')
            newPHP = input('请输入学生php成绩：')
            newPython = input('请输入学生python成绩：')
            # 将获取到的用户输入的新成绩全部赋值到新的字典
            newStudent = {"id":id,"sname":sname,"bj":bj,'stuNum':stuNum,'Linux':newLinux,'PHP':newPHP,'Python':newPython}
            stu_info[stuid].update(newStudent) # 将新字典更新到列表同位置下标下
        else:
            print('学生不存在')


def main():
    while True: 
        menu()
        key = input('请选择功能：')
        if key == '1':
            add_info()
        if key == '2':
            search()
        if key == '3':
            delete()
        if key == '4':
            modify()
        if key == '5':
            show()

        if key == '0':
            break


main()
