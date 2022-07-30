import os
path = input("请输入图片所在文件夹:")# 获取该路径下所有图片
a=1
filelist = os.listdir(path)
for files in filelist:
    # 原始路径
    Olddir = os.path.join(path, files)
    # if os.path.isdir(Olddir):
    # continue
    # 将图片名切片,比如 xxx.bmp 切成xxx和.bmp
     # xxx
    filename = os.path.splitext(files)[0]
    # .bmp
    filetype = os.path.splitext(files)[1]
    # 需要存储的路径 a 是需要定义修改的文件名
    Newdir = os.path.join(path, "图片"+str(a)+ filetype)
    os.rename(Olddir, Newdir)
    a += 1
