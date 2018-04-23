'''
观察引用方式,貌似在这个ide,即使是执行某个子文件.py,执行目录也是工程目录下,所以像下面这样引用
貌似和博客有点差距, 可能是执行路径上不同, 不过由于我的问题暂时解决, 所以先跳过
博客: https://blog.csdn.net/hansel/article/details/8975663
'''

import modelFile.model2 as m2
import sub.modelFile2.model2 as m3
import sub.c as m4  #虽然本文件main.py和c.py处于同一个目录,但是这个ide的执行目录是HowToImport,所以直接import c反而会出错
print(m2.add2(4, 3))
print(m3.add2(4, 3))
print(m4.add2(4, 3))

import sys
print(sys.path)