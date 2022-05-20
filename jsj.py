import math
# 为函数设置了三个参数，并都带有默认参数
def estimated(size=1,number=None,time=None):

     # 人力计算：如果参数中填了时间，没填人数，就是计算人力
    if(number == None) and (time != None):
        number = math.ceil(size * 80/time)
        print('项目大小为{}标准项目，如果在{}个工时完成，则需要人数{}人'.format(size,time,number) )
    # 工时计算器：如果参数中填了人数，没填时间，就是工时计算器
    elif(number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为{}标准项目，如果在{}个工时完成，则需要人数{}人'.format(size,time,number) )

# 调用函数的时候，传递两个参数，会自动计算出第三个参数
while True:
    xuanzhe = int(input('请选择计算器类型：1、人力计算器  2、工时计算器 '))
    if xuanzhe == 1:
        time = float(input('请输入工时：'))
        size = float(input('请输入工程数量：'))
        estimated(size,time)
    elif xuanzhe == 2:
        numbers = float(input('请输入人数：'))
        size = float(input('请输入工程数量：'))
        estimated(size,numbers)
    else:
        print('输入不正确！请重新选择')
    tuichu = input('需要继续吗？请输入1/2')
    if tuichu == '1':
        break
