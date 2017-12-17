import os
import shutil


#1.XX位置是否存在文件夹或者文件
print(os.path.isfile('/home/rong/ccc'))
print(os.path.isdir('/home/rong/cccc'))




#2.删除操作
#删除目录
if os.path.isdir('/home/rong/cccc'):
    shutil.rmtree('/home/rong/cccc') #只能删除目录,删除了目录本身以及目录下的所有文件
    #对于删除目录,建议使用shutil而不是os
    # os好像只能删除空目录,如果想要删除目录下所有文件,还要各种递归操作
    # shutil.rmtree()一句话就搞定了

#删除文件
if os.path.isfile('/home/rong/cc'):
    os.remove('/home/rong/cc')




#3.复制操作
if os.path.isfile('/home/rong/lakeWater.jpg'):
    shutil.copy('/home/rong/lakeWater.jpg', '/home/rong/ccccc') #如果ccccc目录存在,会把文件复制到这个目录下,名字还是lakeWater.jpg
    shutil.copy('/home/rong/lakeWater.jpg', '/home/rong/ccccc/ll.jpg') #复制文件到ccccc目录下,并且命名为ll.jpg
    #附: 如果原来的目录有同名的文件存在, 复制的文件会覆盖之前的文件




#4.创建一个目录
if(not os.path.isdir('/home/rong/c')) and (not os.path.isfile('/home/rong/c')):
    os.mkdir('/home/rong/c') #创建目录,不过必须保证创建位置'/home/rong'不存在同名文件或者同名目录




#5.遍历某个目录
listPath = os.listdir('/home/rong/ccccc')
for path in listPath:
    print('/home/rong/ccccc/' + path)
