# coding=utf-8
import os
for tem in  (r'/gitsome',r'F:\pychram\gitsome'):
    if os.path.isdir(tem):           #如果tem是一个目录的话
        break
else:
    print 'no such directory '
    tem=''

if tem:
    os.chdir(tem)
    cwd=os.getcwd()
    print '当前工作目录：'
    print cwd
    print '创建一个样例目录'
    os.mkdir('example')
    os.chdir('example')
    print '目录创建成功'
    cwd=os.getcwd()
    print cwd
    print '当前目录文件：'
    print os.listdir(cwd)

    print '创建一个测试文件'
    f=file('ftest.txt','w+')
    f.write('first \n')
    f.write('second \n')
    f.close()
    print '创建成功'
    print '当前目录文件'
    print os.listdir(cwd)

    print '重命名'
    os.rename('ftest.txt','test.txt')
    print '当前目录文件'
    print os.listdir(cwd)

    print '文件路径'
    path=os.path.join(cwd,os.listdir(cwd)[0])
    print path
    print '路径，文件名'
    print os.path.split(path)
    print '文件名，格式'
    print os.path.splitext(path)

    print '输出文件'
    f=open('test.txt','r')
    for i in f:
        print i
    f.close()

    print '移除文件'
    os.remove(path)
    print '移除成功'
    print '当前目录文件'
    print os.listdir(cwd)
    print '移除目录'
    os.chdir(r'F:\pychram\gitsome')
    os.rmdir('example')
    print '移除目录成功'
    print '完成'

