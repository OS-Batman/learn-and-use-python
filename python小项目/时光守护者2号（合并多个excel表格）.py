#原程序来自：https://blog.csdn.net/qq_41797451/article/details/80541089
#对程序略作修改，该程序会删去多个excel中重复的行
#导入需要使用的包
import xlrd2  #读取Excel文件的包
import xlsxwriter   #将文件写入Excel的包
import os
#打开一个excel文件
def open_xls(file):
    f = xlrd2.open_workbook(file)
    return f
#获取excel中所有的sheet表
def getsheet(f):
    return f.sheets()
#获取sheet表的行数
def get_Allrows(f,sheet):
    table=f.sheets()[sheet]
    return table.nrows
#读取文件内容并返回行内容
def getFile(file,shnum):
    f=open_xls(file)
    table=f.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row)
        datavalue.append(rdata)
    return datavalue
#获取sheet表的个数
def getshnum(f):
    x=0
    sh=getsheet(f)
    for sheet in sh:
        x+=1
    return x
#函数入口
if __name__ == '__main__':
    # 定义要合并的excel文件列表
    path = r'C:\Users\Admin\Desktop\python-excel'
    allxls = os.listdir(path)
    # 存储所有读取的结果
    datavalue = []
    for onexls in allxls:
        fl = os.path.join(path, onexls)
        f = open_xls(fl)
        x = getshnum(f)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            lst=getFile(fl,shnum)
            rvalue = []
            for el in lst:
                if el not in rvalue:
                    rvalue.append(el)
    endfile= r'C:\Users\Admin\Desktop\python-excel\合并excel.xls'
    wb=xlsxwriter.Workbook(endfile)
    #创建一个sheet工作对象
    ws=wb.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c=rvalue[a][b]
            ws.write(a,b,c)
    wb.close()
    print("文件合并完成")