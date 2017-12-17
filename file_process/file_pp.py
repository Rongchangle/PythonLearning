import math
import os
import shutil



#把三位数字符串(有前导零)转换成数字
def f(s):
    return 100*int(s[0]) + 10 * int(s[1]) + int(s[2])


#把数字(不能超过3位)转换成三位字符串,不足三位的数字转换后要带前导零
def g(num):
    s1 = num % 10
    s3 = math.floor(num/100)
    s2 = math.floor((num - s3 * 100)/10)
    return str(s3) + str(s2) + str(s1)


#删除目录dir,然后新建同名的dir,必须保证dir存在而且是目录,不然报错
#这相当于清空了目录dir
def rebuild(dir):
    shutil.rmtree(dir)
    os.mkdir(dir)


def do_it():
    Path = '/media/rong/学习资料和娱乐/工作/dataset'
    otherPath = '/media/rong/学习资料和娱乐/scut_data_set'

    list1 = ['front1-40','left1-40','right1-40']
    for i in range(3):
        Path2 = Path + '/' + list1[i]
        print(Path2)
        #开始遍历人
        listPath = os.listdir(Path2)
        for p1 in listPath:
            Path3 = Path2 + '/' + p1  # front1-40/1

            listPath2 = os.listdir(Path3)
            for p2 in listPath2:
                Path4 = Path3 + '/' + p2 # front1-40/1/angry

                #清空当前目录,把XX目录下的7个文件复制过来
                otherPath4 = otherPath + '/' + list1[i] + '/' + p1 + '/' + p2

                kkk = False

                if(p2 == 'neutral' and kkk):
                    rebuild(Path4)

                    id = 1 #代表当前图片id
                    c = 0 #代表当前复制图片数目

                    while(c < 7):
                        print(Path4 + '/' + g(id) + '.jpg')
                        if(os.path.isfile(otherPath4 + '/' + g(id) + '.jpg')):
                            shutil.copy(otherPath4 + '/' + g(id) + '.jpg', Path4 + '/' + g(id) + '.jpg')

                            id = id + 3
                            c = c + 1
                        else:
                            id = id + 1

                else:
                    listName = []
                    kk = False
                    if(os.path.isdir(Path4 + '/' + '新建文件夹') and kk):

                        listPath5 = os.listdir(Path4 + '/' + '新建文件夹')

                        print('----------')
                        rebuild('/home/rong/kkkk')
                        for p3 in listPath5: #p3: 003.jpg
                            Path5 = Path4 + '/新建文件夹/' + p3
                            shutil.copy(Path5,'/home/rong/kkkk/' + p3) #先把图片存放到其他地方

                        rebuild(Path4)
                        listPath5 = os.listdir('/home/rong/kkkk')
                        for p3 in listPath5:  # p3: 003.jpg
                            shutil.copy('/home/rong/kkkk/' + p3, Path4 + '/' + p3)

                        print(Path4)

                    else: # 文件夹下有4个文件的情况
                        listPath4 = os.listdir(Path4) #Path4 是 xxx/happy,xxx/sad这些

                        cccc = 1

                        if(len(listPath4) == 4):
                            numlist = []
                            for im in listPath4: # im是002.jpg这些
                                numlist.append(f(im.split('.')[0]))
                                numlist.sort()
                            #numlist里面的是排好序的id(整型变量)

                            if(numlist[3] < 90 and cccc == 1 and False):
                                print(Path4)
                                #第一种复制类型  如果本来是 12, 39, 48, 89
                                # 就把12, 40, 49 复制过来,分别命名为89 + 3 * 14, 89 + 2 * 14, 89 + 14
                                shutil.copy(otherPath4 + '/' + g(numlist[0]) + '.jpg', Path4 + '/' + g(numlist[3] + 14 * 3) + '.jpg')
                                shutil.copy(otherPath4 + '/' + g(numlist[1] + 1) + '.jpg', Path4 + '/' + g(numlist[3] + 14 * 2) + '.jpg')
                                shutil.copy(otherPath4 + '/' + g(numlist[2] + 1) + '.jpg', Path4 + '/' + g(numlist[3] + 14 * 1) + '.jpg')


                            elif(numlist[3] >= 90):
                                #另外一种, 如果本来是56, 89, 110, 134
                                #就把134, 109, 88 复制过来, 改为56 - 3 * 2, 56 - 2* 2, 56 - 1 * 2
                                if(os.path.isfile(otherPath4 + '/' + g(numlist[3]) + '.jpg')):
                                    shutil.copy(otherPath4 + '/' + g(numlist[3]) + '.jpg',
                                                Path4 + '/' + g(numlist[0] - 2 * 3) + '.jpg')
                                    shutil.copy(otherPath4 + '/' + g(numlist[2] - 1) + '.jpg',
                                                Path4 + '/' + g(numlist[0] - 2 * 2) + '.jpg')
                                    shutil.copy(otherPath4 + '/' + g(numlist[1] - 1) + '.jpg',
                                                Path4 + '/' + g(numlist[0] - 2 * 1) + '.jpg')


                        elif(len(listPath4) == 7):

                            numlist = []
                            for im in listPath4:  # im是002.jpg这些
                                numlist.append(f(im.split('.')[0]))
                                numlist.sort()
                            if(numlist[6] - numlist[5] == 14 and numlist[5] - numlist[4] == 14 and numlist[4] - numlist[3] == 14 and False):
                                shutil.copy(otherPath4 + '/' + g(numlist[0]) + '.jpg',
                                            Path4 + '/' + g(numlist[3] + 14 * 3) + '.jpg')
                                shutil.copy(otherPath4 + '/' + g(numlist[1] + 1) + '.jpg',
                                            Path4 + '/' + g(numlist[3] + 14 * 2) + '.jpg')
                                shutil.copy(otherPath4 + '/' + g(numlist[2] + 1) + '.jpg',
                                            Path4 + '/' + g(numlist[3] + 14 * 1) + '.jpg')
                        elif(len(listPath4)!=7):
                            print(Path4,len(listPath4))





#shutil.rmtree('/home/rong/ccc')
shutil.copy('/home/rong/TMD','/home/rong/ccc/102')


do_it()
