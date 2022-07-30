import os
weight=input("请输入你的体重（kg）\n")
height=input("请输入你的身高（cm）\n")
age=input("请输入你的年龄（岁）\n")
exercise=input("请输入你每周锻炼的次数\n")
w=int(weight)
h=int(height)
a=int(age)
e=int(exercise)
if e==0:
    coefficient=1.2
elif e>0 and e<=2:
    coefficient = 1.375
elif e>2 and e<=5:
    coefficient = 1.55
elif e>=6:
    coefficient = 1.725
calories=(90+4.8*h+13.4*w-5.7*a)*coefficient
cal=int(calories)
print("你每天消耗的热量为"+str(cal)+"kcal")
os.system("pause")
#pyinstaller -F kill_myself(热量消耗计算).py
