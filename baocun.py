#!/uer/bin/env python3

def a(): 
         #userdir = input('请确认目录 默认同级目录：') 
         username = input('请输入姓名：') 
         userage = input('请输入年龄：') 
         usersex = input('请输入性别：') 
         #if userdir='': 
          #   userdir='./abc.txt' 
         #else: 
          #   userdir= input('') 
         userinfo = [username,userage,usersex] 
         usertxt = open('./abc.txt','w+') 
         usertxt.write(str(userinfo)) 
         usertxt.close() 



a()