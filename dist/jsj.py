# import math
# # 为函数设置了三个参数，并都带有默认参数
# def estimated(size=1,number=None,time=None):
#
#      # 人力计算：如果参数中填了时间，没填人数，就是计算人力
#     if(number == None) and (time != None):
#         number = math.ceil(size * 80/time)
#         print('项目大小为{}标准项目，如果在{}个工时完成，则需要人数{}人'.format(size,time,number) )
#     # 工时计算器：如果参数中填了人数，没填时间，就是工时计算器
#     elif(number != None) and (time == None):
#         time = size * 80 / number
#         print('项目大小为{}标准项目，如果在{}个工时完成，则需要人数{}人'.format(size,time,number) )
#
# # 调用函数的时候，传递两个参数，会自动计算出第三个参数
# while True:
#     xuanzhe = int(input('请选择计算器类型：1、人力计算器  2、工时计算器 \n'))
#     if xuanzhe == 1:
#         time = float(input('请输入工时：'))
#         size = float(input('请输入工程数量：'))
#         estimated(size,time)
#     elif xuanzhe == 2:
#         numbers = float(input('请输入人数：'))
#         size = float(input('请输入工程数量：'))
#         estimated(size,numbers)
#     else:
#         print('输入不正确！请重新选择')
#     tuichu = input('需要继续吗？请输入Y/N')
#     if tuichu == 'Y':
#         break
# import random
# appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']
# def coupon(money):
#     if money < 5:
#         a = random.choice(appetizer)
#         return a, ''
#     elif 5 <= money <10:
#         b = random.choice(appetizer)
#         return b, '溏心蛋'
# diah,egg = coupon(9)
# print(diah)
# print(egg)
#
# def div(num1, num2):
#     growth = (num1 - num2) / num2
#     percent = str(growth * 100) + '%'
#     return percent
#
#
# def warning():
#     print('Error:你确定上月没赚钱？')
#
#
# def main():
#     while True:
#         num1 = float(input('请输入本月的利润'))
#         num2 = float(input('请输入上月利润'))
#
#         if num2 == 0:
#             warning()
#         else:
#             print('本月的利润增长率：' + div(num1, num2))
#             break
#
#
# main()
class Chinese:
    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里'% area)
class cantnses(Chinese):
    def land_area(self,area,reat = 0.0188):
        Chinese.land_area(self,area*reat)
gonger = Chinese()
yewen = cantnses()
gonger.land_area(960)
yewen.land_area(960)