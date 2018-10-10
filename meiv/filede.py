# !/usr/bin/env python2
# -*-encoding:utf-8-*-

import os,sys
def listdir(dir,file):
    file.write(dir +'\n')
    fielnum =0
    list = os.listdir(dir)#列出目录下的所有文件和目录
    for line in list:
        filepath = os.path.join(dir,line)
        if os.path.isdir(filepath):#如果filepath是目录，则再列出该目录下的所有文件
            listdir(dir+'\\'+line,file)
#            myfile.write(' '+ line +'//'+'\n')
#            for li in os.listdir(filepath):
#                myfile.write('    '+li +'\n')
#                fielnum = fielnum +1
        elif os.path:#如果filepath是文件，直接列出文件名
            myfile.write(' '+line +'\n')
            fielnum = fielnum +1
    myfile.write('all the file num is '+ str(fielnum))
dir = input('please input the path:')
path='C:\Python27'
myfile = open('list.txt','w')
listdir(dir,myfile)
myfile.close()

